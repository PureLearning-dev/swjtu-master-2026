package learncore;

import java.util.StringJoiner;

public class string {
    public static void main(String[] args) {
        // StringBuilder，可以视为一个容器，可以更好地拼接，倒置等操作
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("刘杰");
        stringBuilder.append("龚媛");

        System.out.println(stringBuilder);

        // StringJoiner
        StringJoiner stringJoiner = new StringJoiner(",", "[", "]");
        stringJoiner.add("刘杰").add("龚媛");

        System.out.println(stringJoiner);
        System.out.println("比较字符串");

        compareString();

        splicing();
    }

    public static void compareString(){
        String a = "liujie";
        String b = "liujie";
        // 当直接对变量进行赋值会复用字符串池，使用 new，会重新开辟地址空间
        // 使用 == 比较分为基础类型和引用类型
        // 1. 基础类型比较值
        // 2. 引用类型比较地址
        // 所以一般使用引用类型，都是使用 equals 方法进行比较

        String c = new String("liujie");
        String d = new String("liujie");
        System.out.println(a == b);
        System.out.println(a.equals(b));
        System.out.println(c == d);
        System.out.println(c.equals(d));
    }

    public static void splicing(){
        String a = "ab";
        String b = "cd";
        String ab = "abcd";
        // 使用变量进行拼接则会创建新的地址空间，而使用字符串直接拼接会进行复用字符串池
        System.out.println(a + b == ab);
        System.out.println("ab" + "cd" == ab);
    }
}
