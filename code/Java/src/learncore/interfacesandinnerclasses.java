package learncore;

interface Swim{
    void swim();
}

interface inter{
    void run();
    void test();

    // 在接口中也可以定义函数体，使用 default 关键词
    default int add(int a, int b){
        return a + b;
    }
    // 在接口中也可以定义静态函数，使用 static 关键词
    static int plus(int a, int b){
        return a * b;
    }

    // 上述的两个方式都是定义的 public，默认的
    // 在接口中还可以实现 private
    private int sub(int a, int b){
        return a - b;
    }
    private static int pow(int a){
        int result = 1;
        for(int i = 0; i < a; i++){
            result *= a;
        }
        return result;
    }

    // 因为 private 只有在本类中进行访问，所以私有普通方法只能在默认方法中使用
    // 私有静态方法只有在静态方法中使用
}

// 使用抽象类进行空实现，后续可以实现子类需要什么方法就实现什么方法
abstract class interAapter implements inter {
    @Override
    public void run() {

    }

    @Override
    public void test() {

    }
}

// 只要涉及到类之间的继承和接口之间的继承都是使用 extends
// 类实现接口才使用 implements
// 这样的实现被称为适配器模式
class interClass extends interAapter{
    // 在这个类中想使用 run 方法，则就实现该方法

    @Override
    public void run() {
        System.out.println("Run");
    }
}

class Car{
    private Engine engine;

    // Engine 属于成员内部类
    public class Engine{
        private String version;
        private int price;

        // 在成员内部类中可以通过 外部类名.this.xxx 访问外部类的内容
        public void outer(){
            System.out.println(Car.this.engine);
        }

        public Engine(String version, int price){
            System.out.println("Engine 构造函数执行");
            this.version = version;
            this.price = price;
        }

        public String toString(){
            return "Engine(" + this.version + ", " + this.price + ")";
        }
    }

    // Tire 属于静态内部类
    public static class Tire{
        private String brand;

        public static void run(){
            System.out.println("汽车的轮胎正在运行");
        }
    }

    // 通过方法返回一个内部类实例
    public Engine getEngine(String version, int price){
        return new Engine(version, price);
    }

    public Car(){
        System.out.println("Car 构造函数执行");
        this.engine = new Engine("特斯拉", 20000);
    }

    public String toString(){
        return "Car(" + this.engine.toString() + ")";
    }

    // 局部内部类和匿名内部类，前者是在方法中的类，后者是前者没有名称的形式
    // 匿名内部类必然有继承实现关系，或是类或是接口
    public void swim(Swim swim){
        swim.swim();
    }
}

public class interfacesandinnerclasses {
    public static void main(String[] args) {
        interClass interClass = new interClass();
        interClass.run();

        Car car = new Car();
        // 成员内部类的初始化
        // Engine 必须隶属于一个外部类的实例对象，所以才先 new 一个 Car
        Car.Engine engine = new Car().new Engine("华为", 92011);

        System.out.println(car);
        System.out.println(engine);

        // 实例静态内部类
        Car.Tire tire = new Car.Tire();

        car.swim(new Swim() {
            @Override
            public void swim() {
                System.out.println("Car 中的 swim 方法中传递的匿名内部类实现的 swim 方法");
            }
        });
    }
}
