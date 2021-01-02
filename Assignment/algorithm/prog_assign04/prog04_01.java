import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;

public class prog04_01 {

    static Scanner sc = new Scanner(System.in);

    public static class Person {
        String Name;
        String Company;
        String Address;
        String Zipcode;
        String Phones;
        String Email;

        public Person(String Name, String Company, String Address, String Zipcode, String Phones, String Email) {
            this.Name = Name;
            this.Company = Company;
            this.Address = Address;
            this.Zipcode = Zipcode;
            this.Phones = Phones;
            this.Email = Email;
        }
    }

    protected static class Node {
        protected Person data;
        protected Node left;
        protected Node right;
        protected Node p;

        public Node(Person data) {
            this.data = data;
            left = null;
            right = null;
            p = null;
        }
    }

    public static void main(String[] args) throws IOException {
        Person[] person = new Person[500];
        int i = 0;
        System.out.print("$ ");
        sc.next();
        String fileName = sc.next();
        BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\박가연\\Desktop\\" + fileName));
        String line = br.readLine();
        while (true) {//토큰 나누기
            line = br.readLine();
            if (line == null)
                break;
            String sName, sCompany, sAddress, sZipcode, sPhones, sEmail;
            int cnt = cntLine(line);
            if (cnt == 2) {
                StringTokenizer st = new StringTokenizer(line, "\"");
                String token1 = st.nextToken();
                sAddress = st.nextToken();
                String token3 = st.nextToken();

                st = new StringTokenizer(token1, ",");
                sName = st.nextToken();
                sCompany = st.nextToken();

                st = new StringTokenizer(token3, ",");
                sZipcode = st.nextToken();
                sPhones = st.nextToken();
                sEmail = st.nextToken();
            } else if (cnt == 4) {
                StringTokenizer st = new StringTokenizer(line, "\"");
                String token1 = st.nextToken();
                sCompany = st.nextToken();
                String token3 = st.nextToken();
                sAddress = st.nextToken();
                String token5 = st.nextToken();

                st = new StringTokenizer(token1, ",");
                sName = st.nextToken();
                st = new StringTokenizer(token5, ",");
                sZipcode = st.nextToken();
                sPhones = st.nextToken();
                sEmail = st.nextToken();
            } else {
                StringTokenizer st = new StringTokenizer(line, ",");
                sName = st.nextToken();
                sCompany = st.nextToken();
                sAddress = st.nextToken();
                sZipcode = st.nextToken();
                sPhones = st.nextToken();
                sEmail = st.nextToken();
            }
            person[i++] = new Person(sName, sCompany, sAddress, sZipcode, sPhones, sEmail);
        }
        br.close();

        Node root = new Node(person[0]);
        for (int j = 1; j < 500; j++) {
            Insert(root, person[j]);
        } //저장
        while (true) { //프로그램 실행시작
            System.out.print("$ ");
            String order = sc.next();

            if (order.equals("exit"))
                return;
            else if (order.equals("delete")) {
                String deleteName = sc.next();
                delete(find(root, deleteName));
            } else if (order.equals("find")) {
                String searchName = sc.next();
                Node searchNode = find(root, searchName);
                if (searchNode == null)
                    System.out.println("존재하지 않습니다.");
                else
                    printNode(searchNode);
            } else if (order.equals("trace")) {
                String traceName = sc.next();
                trace(root, traceName);
            } else if (order.equals("list")) {
                list(root);
            } else if (order.equals("save")) {
                fileName = sc.next();
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("C:\\Users\\박가연\\Desktop\\" + fileName), "MS949"));
                bw.write("name,company_name,address,zip,phone,email");
                bw.write("\n");
                save(root, bw);
                bw.close();
            } else {
                System.out.println("잘못된 입력입니다.");
            }
        }
    }

    public static Node Insert(Node root, Person data) {
        Node t = root;
        Node y = null;
        Node node = new Node(data);
        while (t != null) {
            if (t.data.Name == node.data.Name)
                return t;
            y = t;
            if (y.data.Name.compareTo(node.data.Name) > 0)
                t = y.left;
            else
                t = y.right;

        }
        if (y.data.Name.compareTo(node.data.Name) > 0)
            y.left = node;
        else
            y.right = node;
        node.p = y;
        return root;
    }

    public static int cntLine(String line) {

        int cnt = 0;
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '"')
                cnt++;
            if (cnt == 4)
                break;
        }
        return cnt;
    }

    public static Node find(Node root, String name) {
        Node t = root;
        while (t != null) {
            if (name.equals(t.data.Name))
                return t;
            else {
                if (t.data.Name.compareTo(name) > 0)
                    t = t.left;
                else
                    t = t.right;
            }
        }
        return null;
    }

    public static Node delete(Node t) {
        if (t.right == null && t.left == null) { //자식이 없을경우
            if (t.p.left == t)
                t.p.left = null;
            else
                t.p.right = null;
        } else if (t.right != null && t.left != null) { //자식이 둘다 있을경우
            t.data = successor(t).data;
            delete(successor(t));
        } else { //자식이 하나
            if (t.left == null) { //오른쪽 자식이 있을경우
                if (t.p.left == t) {
                    t.p.left = t.right;
                } else
                    t.p.right = t.right;
            } else { //왼쪽자식이 있을경우
                if (t.p.left == t) {
                    t.p.left = t.left;
                } else
                    t.p.right = t.left;
            }
        }
        return t;
    }

    public static Node successor(Node t) {
        if (t.right != null) {
            return Minimum(t.right);
        }
        Node y = t.p;
        while (y != null && t == y.right) {
            t = y;
            y = y.p;
        }
        return y;
    }

    public static Node Minimum(Node t) {
        while (t.left != null) {
            t = t.left;
        }
        return t;
    }

    public static void trace(Node root, String name) {
        Node t = root;
        while (t != null) {
            if (name.equals(t.data.Name)) {
                System.out.println(t.data.Name);
                return;
            } else {
                System.out.println(t.data.Name);
                if (t.data.Name.compareTo(name) > 0)
                    t = t.left;
                else
                    t = t.right;
            }
        }
    }

    public static void list(Node t) {
        if (t == null)
            return;
        list(t.left);
        printNode(t);
        list(t.right);
    }

    public static void save(Node root, BufferedWriter bw) throws IOException {
        if (root == null)
            return;
        save(root.left, bw);
        if (root.data.Company.contains(",") && root.data.Address.contains(","))
            bw.write(root.data.Name + ",\"" + root.data.Company + "\",\"" + root.data.Address + "\"," + root.data.Zipcode + "," + root.data.Phones + "," + root.data.Email);
        else if (root.data.Company.contains(","))
            bw.write(root.data.Name + ",\"" + root.data.Company + "\"," + root.data.Address + "," + root.data.Zipcode + "," + root.data.Phones + "," + root.data.Email);
        else if (root.data.Address.contains(","))
            bw.write(root.data.Name + "," + root.data.Company + ",\"" + root.data.Address + "\"," + root.data.Zipcode + "," + root.data.Phones + "," + root.data.Email);
        else
            bw.write(root.data.Name + "," + root.data.Company + "," + root.data.Address + "," + root.data.Zipcode + "," + root.data.Phones + "," + root.data.Email);
        bw.write("\n");
        save(root.right, bw);
    }

    public static void printNode(Node root) {
        System.out.println(root.data.Name);
        System.out.println("\tCompany: " + root.data.Company);
        System.out.println("\tAddress: " + root.data.Address);
        System.out.println("\tZipcode: " + root.data.Zipcode);
        System.out.println("\tPhones: " + root.data.Phones);
        System.out.println("\tEmail: " + root.data.Email);
    }
}