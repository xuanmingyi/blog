Title: Golang Slice切片(4)
Date: 2021-06-08 22:13:03
Tags: Golang
Slug: golang-slice
Authors: sin
Summary: Golang 标准库slice

### 基本操作

**slice**的基础操作, 切片有固定长度，不可改变。

    :::go
    var aSlice []int
    fmt.Println(aSlice == nil)  // true
    aSlice = make([]int, 100)
    fmt.Println(aSlice == nil)  // false

    //aSlice[100] = 100  // panic: runtime error: index out of range [100] with length 100 错误，不能超出长度

### len和cap

当使用**append**来给**slice**添加元素的时候，超过cap的时候，会触发copy

    :::go
    var aSlice []int

    aSlice = make([]int, 10, 11)
    fmt.Println(&aSlice[0])       // 0xc0000200c0

    aSlice = append(aSlice, 10)
    fmt.Println(&aSlice[0])       // 0xc0000200c0

    aSlice = append(aSlice, 20)
    fmt.Println(&aSlice[0])       // 0xc00009e000

### 遍历

    :::go
    for index, value := range aSlice {
        fmt.Println(index, value)
    }

这里特别要注意的是value是aSlice中的数据的复制，举一个例子。下面这个例子遍历的其实是对象的地址。So，每一个数据的Age被改成100。

    :::go
    type User struct {
        Name string
        Age int
    }

    func main() {
        users := []*User{ &User{Name: "John"}, &User{Name: "HanMeimei"} }
        for _, value := range users {
            value.Age = 100
        }
        for _, value1 := range users {
            fmt.Println(*value1)
        }
    }

### 增、删、改、查

    :::go
    aSlice := make([]int, 0)
    aSlice = append(aSlice, 10, 20, 30, 40, 50) // 增加元素  [10, 20, 30, 40, 50]
    aSlice = append(aSlice, []int{60, 70, 80}...) // 增加元素  [10, 20, 30, 40, 50, 60, 70, 80]

    aSlice = aSlice[2:]                         // 删除开头2个元素 [30, 40, 50, 60, 70, 80]
    aSlice = append(aSlice[:0], aSlice[2:]...)  // 删除开头2个元素，一个0长度切片和后面元素结合
    aSlice = aSlice[:copy(aSlice, aSlice[2:])]  // 删除开头2个元素，copy返回copy元素数量 

    aSlice = append(aSlice[:2], aSlice[4:]...)          // 删除中间2个元素 [10, 20, 50, 60, 70, 80, 90]
    aSlice = aSlice[:2 + copy(aSlice[2:], aSlice[4:])]  // 删除中间2个元素
    aSlice = aSlice[:len(aSlice) - 2] // 删除末尾2个元素
    aSlide[2] = 10 // 改元素

    // 查找元素,返回索引
    func Find(aSlice []int, v int) (index int) {
        for index, value := range aSlice {
            if value == v {
                return index
            }
        }
        return -1
    }