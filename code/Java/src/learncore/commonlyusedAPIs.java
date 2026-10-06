package learncore;


import java.io.IOException;
import java.math.BigInteger;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Calendar;
import java.util.Date;
import java.util.Random;

public class commonlyusedAPIs implements Cloneable{
    public static void main(String[] args) throws IOException, ParseException {
        // Math 中存在许多数学静态方法
        System.out.println(Math.abs(-1));

        // System 中存在使用的三个方法
        // 1. 获取当前时间对应的毫秒值
        System.out.println(System.currentTimeMillis());
        // 2. 终止当前 JVM 执行，0 表示正常退出
        if(args.length != 0 && args[0].equals("0")){
            System.exit(0);
        }
        // 3. 数值元素拷贝
        // 基础类型是必须类型相同，引用类型源数组可以是目标数组的子类型
        // 且引用类型进行拷贝是浅拷贝
        int[] src = new int[]{1, 2, 3, 4, 5};
        int[] dest = new int[3];
        System.arraycopy(src, 1, dest, 0, 3);
        for(int i : dest){
            System.out.println(i);
        }

        // Runtime 类可以执行一些关于运行时的命令和得到一些相关数据
        Runtime runtime = Runtime.getRuntime();
        System.out.println(runtime);
        System.out.println(runtime.availableProcessors());
        System.out.println(runtime.maxMemory());
        System.out.println(runtime.totalMemory());
        System.out.println(runtime.freeMemory());
        // 执行 cmd 命令
        System.out.println(runtime.exec("ls"));

        // Object 相关方法
        // public String toString()    //返回该对象的字符串表示形式(可以看做是对象的内存地址值)
        // public boolean equals(Object obj)    //比较两个对象地址值是否相等；true表示相同，false表示不相同
        // protected Object clone()    //对象克隆

        // Objects 相关的方法
        // public static String toString(Object o) // 获取对象的字符串表现形式
        // public static boolean equals(Object a, Object b) // 比较两个对象是否相等
        // public static boolean isNull(Object obj)  // 判断对象是否为null
        // public static boolean nonNull(Object obj) // 判断对象是否不为null
        // public static <T> T requireNonNull(T obj)  // 检查对象是否不为null,如果为null直接抛出异常；如果不是null返回该对象；
        // public static <T> T requireNonNullElse(T obj, T defaultObj) // 检查对象是否不为null，如果不为null，返回该对象；如果为null返回defaultObj值
        // public static <T> T requireNonNullElseGet(T obj, Supplier<? extends T> supplier) // 检查对象是否不为null，如果不为null，返回该对象；如果为null,返回由Supplier所提供的值

        // 还有 BigInteger 和 BigDecimal 两个类的使用
        // 前者是用于大整数计算和表达的，后者是用于高精度小数表达和计算的
        BigInteger bigInteger = new BigInteger(5, new Random());
        System.out.println(bigInteger);
        BigInteger bigInteger1 = new BigInteger("292019400293093", 16);
        System.out.println(bigInteger1);
        BigInteger bigInteger2 = new BigInteger("524342313445352323523");
        BigInteger bigInteger3 = new BigInteger("394892837982738578375");
        // 保留整数部分
        System.out.println(bigInteger2.divide(bigInteger3));

        // 在 BigInteger 实例对象上存在许多用于计算操作的方法
        // BigDecimal 和 BigInteger 类似，但是对于除法需要注意保留位数和取舍模式

        // Date 类
        Date date = new Date();
        System.out.println(date);
        // 也可以传入毫秒值得到一个 Date 对象
        Date date1 = new Date(System.currentTimeMillis());
        System.out.println(date1);
        System.out.println(date.getTime());
        System.out.println(System.currentTimeMillis());
        // 对 Date 对象设置毫秒值
        date.setTime(1);
        System.out.println(date);

        // SimpleDateFormat 类，对 Date 进行格式化转换
        SimpleDateFormat format = new SimpleDateFormat("yyyy年MM月dd日 HH时mm分ss秒");
        System.out.println(format.format(date1));
        // 将字符串解析为 Date 对象
        String date3 = "2004年8月1日 24时48分21秒";
        System.out.println(format.parse(date3));

        // Calendar类，日历类，可以进行日期计算
        Calendar calendar = Calendar.getInstance();
        System.out.println(calendar);
        System.out.println(calendar.getTime());
        // 在 calendar 的基础上修改字段值
        calendar.add(Calendar.DAY_OF_MONTH, 3);
        System.out.println(calendar.getTime());

        System.out.println(ZoneId.getAvailableZoneIds());
        System.out.println(ZoneId.systemDefault());

        // 现在都使用 Local 这一套 API 了
        LocalDateTime localeDateTime = LocalDateTime.now();
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd-HH:mm:ss");
        System.out.println(localeDateTime.format(dateTimeFormatter));

        // 时区，在一个时区的时间换到另一个时区，是不同的
        ZonedDateTime shanghai = ZonedDateTime.of(localeDateTime, ZoneId.systemDefault());
        System.out.println(shanghai);
        ZonedDateTime la = shanghai.withZoneSameInstant(ZoneId.of("America/Los_Angeles"));
        System.out.println(la);

        // 得到标准时间的 Instance 对象，表示在世界绝对时间线上的一点
        Instant instant = Instant.now();
        System.out.println(instant);

        // Duration 表示时间间隔，单位是小时，分钟，秒
        // Period 也表示时间间隔，单位是年，月，日
        // ChronoUnit 是上面两个的组合
        LocalDateTime birthday = LocalDateTime.of(2004, 8, 1, 11, 34);
        LocalDateTime today = LocalDateTime.now();
        Duration duration = Duration.between(birthday, today);
        System.out.println(duration);
        System.out.println(duration.toDays());
        System.out.println(duration.toDays() / 365);

        LocalDate localDate = LocalDate.now();
        LocalDate pastDate = LocalDate.of(2004, 8, 1);
        Period period = Period.between(pastDate, localDate);
        System.out.println(period);
        System.out.println(period.getYears());

        //System.out.println("相差的年数:" + ChronoUnit.YEARS.between(birthDate, today));
        //System.out.println("相差的月数:" + ChronoUnit.MONTHS.between(birthDate, today));
        //System.out.println("相差的周数:" + ChronoUnit.WEEKS.between(birthDate, today));
        //System.out.println("相差的天数:" + ChronoUnit.DAYS.between(birthDate, today));
        //System.out.println("相差的时数:" + ChronoUnit.HOURS.between(birthDate, today));
        //System.out.println("相差的分数:" + ChronoUnit.MINUTES.between(birthDate, today));
        //System.out.println("相差的秒数:" + ChronoUnit.SECONDS.between(birthDate, today));
        //System.out.println("相差的毫秒数:" + ChronoUnit.MILLIS.between(birthDate, today));
        //System.out.println("相差的微秒数:" + ChronoUnit.MICROS.between(birthDate, today));
        //System.out.println("相差的纳秒数:" + ChronoUnit.NANOS.between(birthDate, today));
        //System.out.println("相差的半天数:" + ChronoUnit.HALF_DAYS.between(birthDate, today));
        //System.out.println("相差的十年数:" + ChronoUnit.DECADES.between(birthDate, today));
        //System.out.println("相差的世纪(百年)数:" + ChronoUnit.CENTURIES.between(birthDate, today));
        //System.out.println("相差的千年数:" + ChronoUnit.MILLENNIA.between(birthDate, today));
        //System.out.println("相差的纪元数:" + ChronoUnit.ERAS.between(birthDate, today));
        LocalDateTime llago = LocalDateTime.of(-100000, 3, 1, 3, 4);
        LocalDateTime now = LocalDateTime.now();
        long chronoUnit = ChronoUnit.MILLENNIA.between(llago, now);
        System.out.println(chronoUnit);
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        // 可以在这里自己实现深拷贝的成员变量
        return super.clone();
    }
}
