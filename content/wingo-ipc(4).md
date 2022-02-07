Title: Wingo-ipc(4)
Date: 2021-09-27 04:44:52
Tags: Wingo
Slug: wingo-ipc-4
Authors: sin
Summary: Wingo IPC机制的研究

### gribble库学习

[gribble](https://github.com/BurntSushi/gribble)在wingo中被使用，这个库其实只是完成一个代码组织，使系统其他部分可以通过一个**字符串**来调用到对应的代码。



#### 服务器代码

    :::go
    package main

    import (
        "bufio"
        "fmt"
        "io"
        "net"

        "github.com/BurntSushi/gribble"
    )

    type Add struct {
        name string `add`
        Op1  int    `param:"1"`
        Op2  int    `param:"2"`
    }

    func (c Add) Run() gribble.Value {
        return c.Op1 + c.Op2
    }

    var env *gribble.Environment = gribble.New([]gribble.Command{
        Add{},
    })

    func main() {
        conn, err := net.Listen("tcp", ":8888")
        if err != nil {
            panic(err)
        }

        for {

            client, err := conn.Accept()
            if err != nil {
                panic(err)
            }
            go handleClient(client)
        }
    }

    func handleClient(conn net.Conn) {
        defer conn.Close()
        var retVal string

        for {
            // read from connection
            reader := bufio.NewReader(conn)
            msg, err := reader.ReadString(0)
            if err == io.EOF {
                return
            }

            if err != nil {
                panic(err)
            }

            // deal with msg
            msg = msg[:len(msg)-1]

            fmt.Println(msg)

            val, err := env.RunMany(msg)
            if err != nil {
                panic(err)
            }

            if val != nil {
                switch v := val.(type) {
                case string:
                    retVal = v
                case int:
                    retVal = fmt.Sprintf("%d", v)
                }
            }
            fmt.Println(retVal)

            // write to connection
            conn.Write([]byte(retVal))
        }
    }



#### 客户端代码

    :::go
    package main

    import (
        "fmt"
        "net"
    )

    func main() {
        conn, err := net.Dial("tcp", ":8888")
        if err != nil {
            panic(err)
        }
        defer conn.Close()

        _, err = conn.Write([]byte("add 1 3"))
        if err != nil {
            panic(err)
        }
        _, err = conn.Write([]byte{0})
        if err != nil {
            panic(err)
        }

        data := make([]byte, 1024)
        len, err := conn.Read(data)
        if err != nil {
            panic(err)
        }
        fmt.Println(string(data[:len]))
    }

![ipc](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20210927134743.png)

上述项目中，我们通过网络传递了一个**"add 1 3"**的字符串给服务端。

服务端通过预先注册的**gribble.Environment**调用了对应的Run代码。获得数据并返回。



### wingo ipc分析

**wingo ipc**和上述例子类似，但是有几个不同点


* 使用unix socket
* conn写入数据是通过 **fmt.Fprintf**，file就是conn

