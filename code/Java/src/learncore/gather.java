package learncore;

import java.util.*;

public class gather {
    // 集合下有 Collection 和 Map 两个接口，下面有 List 和 Set
    // 前者是单列，也就是类似于 [a, b, c, ...]
    // 后者是双列，也就是类似于 {a: A, b: B, c: C, ...}
    // 前者下面还有两个接口，分别是 List 和 Set，前者可重复，后者不可重复
    // 每个接口下都有其对应的具体实现
    public static void main(String[] args) {
        Collection<Integer> collection = new LinkedList<>();
        for(int i = 0; i < 10; i++){
            collection.add(i);
        }

        Iterator<Integer> iterator = collection.iterator();
        while(iterator.hasNext()){
            Integer next = iterator.next();
            System.out.println(next);
        }
        // 使用迭代器等价于使用强化 for
        // for 循环中的 : 底层就是使用的迭代器
        for(Integer i : collection){
            System.out.println(i);
        }

        // 初始化 Set 不能有重复的元素，创建的是不可遍的对象
        Set<Integer> set = Set.of(1, 2);
        for(Integer i : set){
            System.out.println(i);
        }
        // 添加元素，直接报错
//        set.add(4);

        Map<Integer, String> map = new HashMap<>();
        map.put(1, "刘杰");

        System.out.println(map.values());
    }
}
