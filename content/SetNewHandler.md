Title: set_new_handler demo
Date: 2015-06-27 02:18
Tags: cpp
Authors: Sin
Category: Technology 


set_new_handler小酌

```c++
#include <new>
#include <iostream>
#include <stdlib.h>

using namespace std;

void oom(){
    cout << "Out Of Memory" << endl;
    exit(1);
}

int main(){
    set_new_handler(oom);
    new char[1024*1024*1024*2];
    return 0;
}
```

![](http://i.imgur.com/9pDT39I.gif)
