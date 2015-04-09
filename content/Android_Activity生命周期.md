Title: Android Activity生命周期
Date: 2015-01-17 19:21
Tags: Android
Authors: Sin
Category: Technology

Android App不像其他编程语言一样，从一个main()函数进入，他是由Android系统初始化一个Activity实例，而我们需要做的就是给这个实例写一些回调函数来管理他的整个生命周期。当我们打开或者关闭一个app的时候需要调用一系列的回调。

**回调函数**

回调函数的调用链就像下图的金字塔一样，Activity的每一个状态就是金字塔的一阶，创建一个新的activity，每一个回调函数使activity的状态向上一步，金字塔的最顶端就是activity在最前端运行，可以和用户进行交互。

当用户离开这个activity的时候，系统调用其他方法使activity的状态从顶端一步步下移。在某些情况下,比如当用户换到另一个app的时候,activity不会被销毁,只会移动到Stopped状态,当用户返回时,可以恢复到运行状态。

![](http://ww4.sinaimg.cn/mw690/68ef69degw1eocm6z5z9qj20ie087q4j.jpg)

**状态**

在所有状态中，只有三个状态是稳定状态，其他状态都是短暂的。

 * *Resumed*: activity在最前端，可以和用户交互
 * *Paused*: 被其他activity部分遮挡，不能接收用户的输入和运行任何代码
 * *Stopped*: activity完全在后台运行，但是用户数据被保留

**实验**

对上面提到的各个状态函数实现，然后启动、停止app，观察输出

    public class MainActivity extends Activity {
        private static final String TAG = "Lifecycle";  
    
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            Log.e(TAG, "onCreate");
        }

        @Override
        protected void onResume(){
            super.onResume();
            Log.e(TAG, "onResume");
        }
    
        @Override
        protected void onStart(){
            super.onStart();
            Log.e(TAG, "onStart");
        }
    
        @Override
        protected void onRestart(){
            super.onResume();
            Log.e(TAG, "onRestart");
        }
        
        @Override
        protected void onPause(){
            super.onPause();
            Log.e(TAG, "onPause");
        }
        
        @Override
        protected void onStop(){
            super.onStop();
            Log.e(TAG, "onStop");
        }
    
        @Override
        protected void onDestroy(){
            super.onDestroy();
            Log.e(TAG, "onDestroy");
        }
    }


***实验一***

点击APP图标，APP启动，到*Resumed*状态，顺序调用onCreate() -> onStart() -> onResume()

![](http://ww2.sinaimg.cn/mw690/68ef69degw1eocx8fmk4xj20j703q0sn.jpg)


***实验二***

在实验一的状态下，点击Home键，到*Stopped*状态，顺序调用 onPause() -> onStop()

![](http://ww2.sinaimg.cn/mw690/68ef69degw1eocxrpjglgj20jd02imx0.jpg)

***实验三***

在实验二的状态下，重新点击APP图标， 回到*Resumed*状态， 顺序调用 onRestart() -> onStart() -> onResume()

![](http://ww3.sinaimg.cn/mw690/68ef69degw1eocxw6ydr1j20jd02uwee.jpg)

***实验四***

在实验三的状态下，按返回键，退出APP, 顺序调用 onPause() -> onStop() -> onDestroy()

![](http://ww4.sinaimg.cn/mw690/68ef69degw1eocxzhojy3j20ji02f0sm.jpg)

简单的来说，activity的生命周期如是说。
