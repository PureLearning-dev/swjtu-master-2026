package learncore;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regularexpression {
    // 正则表达式是一种校验字符串的规则，可以通过这个判断一个字符串是否满足我们的需要
    public static void main(String[] args) {
        //找出str中所有的JavaXX
        String str = "Java自从95年问世以来，经历了很多版本，目前企业中用的最多的是Java8和Java11，" +
                "因为这两个是长期支持版本，下一个长期支持版本是Java17，相信在未来不久Java17也会逐渐登上历史舞台";

        //1.获取正则表达式的对象
        Pattern p = Pattern.compile("Java\\d{0,2}");
        //2.获取文本匹配器的对象
        //m:文本匹配器的对象
        //str:大串
        //p:规则
        //拿着m去读取str，找符合p规则的子串
        Matcher m = p.matcher(str);

        //3.利用循环获取
        //find方法：
        //拿着文本匹配器从头开始读取，寻找是否有满足规则的子串
        //如果扫描完字符串还没有，方法返回false
        //如果有，返回true。在底层记录子串的起始索引和结束索引+1，如初始记录0和4
        //后面会依次往后读取，如第二次从4索引开始读取
        //group方法：
        //方法底层会根据find方法记录的索引进行字符串的截取（使用subString方法，初始截取subString(0,4)），并返回截取后的子串
        while (m.find()) {
            String s = m.group();
            System.out.println(s);
        }

        // String 中的 split 和 replaceAll 都可以使用正则表达式
        // 这部分在需要使用的时候进行查阅才是合适的方法，并不需要现在完全熟练掌握
    }
}
