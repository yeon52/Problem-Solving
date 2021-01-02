import java.io.*;
import java.util.*;

public class prog05_01 {
    static Scanner sc = new Scanner(System.in);
    static int i = 0, j = 0, n = 0;
    static Node[] adjacent = new Node[15000]; //인접리스트
    static String[] allName = new String[15000]; //지명
    static String[] allLat = new String[15000]; //위도
    static String[] allLon = new String[15000]; //경도
    static Node p = new Node();
    static String[] visit = new String[15000];
    static Queue q = new LinkedList();
    static PriorityQueue<dist> Q = new PriorityQueue<dist>();

    protected static class Node {
        protected String Name;
        protected double dis; //거리
        protected Node next;

        public Node(String Name, double dis) {
            this.Name = Name;
            this.dis = dis;
            this.next = null;
        }

        public Node() {
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br1 = new BufferedReader(new FileReader("C:\\Users\\박가연\\Desktop\\alabama.txt"));
        String line = new String();
        while (true) {
            line = br1.readLine();
            if (line == null)
                break;
            StringTokenizer st = new StringTokenizer(line, "\t"); //이름, 경도, 위도 토큰나누기
            allName[i] = st.nextToken();
            allLon[i] = st.nextToken();
            allLat[i] = st.nextToken();
            i++;
        }

        String[] tok1 = new String[50000];
        String[] tok2 = new String[50000];
        BufferedReader br2 = new BufferedReader(new FileReader("C:\\Users\\박가연\\Desktop\\roadList2.txt"));
        while (true) {
            line = br2.readLine();
            if (line == null)
                break;
            StringTokenizer st = new StringTokenizer(line, "\t");
            tok1[j] = st.nextToken();
            tok2[j] = st.nextToken();
            j++;
        }

        //인접리스트 생성
        double area1_lat = 0, area1_lon = 0, area2_lat = 0, area2_lon = 0;
        for (int k = 0; k < i; k++) {
            adjacent[k] = new Node();
            adjacent[k].Name = allName[k];
            p = adjacent[k];
            area1_lat = Double.parseDouble(allLat[k]);
            area1_lon = Double.parseDouble(allLon[k]);
            for (int l = 0; l < j; l++) {
                if (tok1[l].equals(allName[k])) {
                    for (int a = 0; a < i; a++) {
                        if (allName[a].equals(tok2[l])) {
                            area2_lat = Double.parseDouble(allLat[a]);
                            area2_lon = Double.parseDouble(allLon[a]);
                        }
                    }
                    Node temp = new Node(tok2[l], calDistance(area1_lat, area1_lon, area2_lat, area2_lon));
                    p.next = temp;
                    p = p.next;
                } else if (tok2[l].equals(allName[k])) {
                    for (int a = 0; a < i; a++) {
                        if (allName[a].equals(tok1[l])) {
                            area1_lat = Double.parseDouble(allLat[a]);
                            area1_lon = Double.parseDouble(allLon[a]);
                        }
                    }
                    Node temp = new Node(tok1[l], calDistance(area1_lat, area1_lon, area2_lat, area2_lon));
                    p.next = temp;
                    p = p.next;
                }
            }
        }

        //실행
        System.out.print("a, b, c 문제 중 선택 : ");
        String e = sc.nextLine();
        if (e.equals("a")) {
            System.out.print("한 지점 입력 : ");
            String name = sc.nextLine();
            for (int k = 0; k < i; k++) {
                if (name.equals(adjacent[k].Name))
                    BFS(k);
            }
        } else if (e.equals("b")) {
            System.out.print("한 지점 입력 : ");
            String name = sc.nextLine();
            for (int k = 0; k < i; k++) {
                if (name.equals(adjacent[k].Name))
                    DFS(adjacent[k]);
            }
            FileWriter writer = new FileWriter("DFS.txt");
            BufferedWriter bw = new BufferedWriter(writer);
            bw.write(dfsSave.toString());
            writer.flush();
            bw.close();
        } else {
            System.out.println("두 지점 입력 : ");
            String name1 = sc.nextLine();
            String name2 = sc.nextLine();
            int a = 0, b = 0;
            for (int k = 0; k < i; k++) {
                if (name1.equals(adjacent[k].Name))
                    a = k;
            }
            for (int k = 0; k < i; k++) {
                if (name2.equals(adjacent[k].Name))
                    b = k;
            }
            Dijkstra(a, b);
        }
    }

    public static double calDistance(double lat1, double lon1, double lat2, double lon2) {
        double theta, dist;
        theta = lon1 - lon2;
        dist = Math.sin(deg2rad(lat1)) * Math.sin(deg2rad(lat2))
                + Math.cos(deg2rad(lat1))
                * Math.cos(deg2rad(lat2)) * Math.cos(deg2rad(theta));
        dist = Math.acos(dist);
        dist = rad2deg(dist);
        dist = dist * 60 * 1.1515;
        dist = dist * 1.609344;

        dist = dist * 1000.0;

        return dist;
    }

    private static double deg2rad(double deg) {
        return (double) (deg * Math.PI / (double) 180);
    }

    private static double rad2deg(double rad) {
        return (double) (rad * (double) 180 / Math.PI);
    }

    public static void BFS(int s) {
        Node tmp = new Node();
        Node p = new Node();
        int[] d = new int[i]; // 현재 노드 길이
        int u; //이전 인덱스
        int v = 0; //현재 인덱스
        for (int k = 0; k < i; k++)
            d[k] = -1;

        q.offer(s);
        d[s] = 0;
        while (!q.isEmpty()) {
            u = (int) q.poll();
            tmp = adjacent[u];
            p = tmp.next;
            while (p != null) {
                for (int k = 0; k < i; k++) {
                    if (p.Name.equals(adjacent[k].Name)) {
                        v = k;
                        break;
                    }
                }
                if (d[v] == -1) { //방문유무 확인
                    d[v] = d[u] + 1; //이전 노드 d+1
                    for (int k = 0; k < i; k++) {
                        if (p.Name.equals(adjacent[k].Name)) {
                            q.offer(k);
                            break;
                        }
                    }
                }
                p = p.next;
            }
        }
        for (int k = 0; k < i; k++) {
            if (d[k] <= 10) {
                for (int m = 0; m < i; m++) {
                    if (adjacent[k].Name.equals(allName[m])) {
                        System.out.println(allName[m] + " " + allLat[m] + " " + allLon[m]); //이름,위도,경도 출력
                        break;
                    }
                }
            }
        }
    }

    public static StringBuilder dfsSave = new StringBuilder();

    public static void DFS(Node v) {
        int chk = 0;
        for (int k = 0; k < n; k++) {
            if (visit[k].equals(v.Name)) {
                chk = 1;
            }
        }
        if (chk == 0) {
            visit[n++] = v.Name;
            for (int k = 0; k < i; k++) {
                if (v.Name.equals(adjacent[k].Name)) {
                    for (int m = 0; m < i; m++) {
                        if (adjacent[k].Name.equals(allName[m])) {
                            dfsSave.append(allName[m]).append(" ").append(allLat[m]).append(" ").append(allLon[m]).append("\n");
                            break;
                        }
                    }
                    break;
                }
            }
            Node u = v.next;
            while (u != null) {
                for (int k = 0; k < i; k++) {
                    if (u.Name.equals(adjacent[k].Name)) {
                        DFS(adjacent[k]);
                        break;
                    }
                }
                u = u.next;
            }
        }
    }

    public static void Dijkstra(int s, int dest) {
        Node tmp = new Node();
        Node p = new Node();
        double[] d = new double[i]; //현재까지의 최소경로
        int u;  //현재 인덱스
        int v = 0, w;
        String path[][] = new String[i][i]; //경로저장
        for (int k = 0; k < i; k++) {
            d[k] = -1;
        }
        Q.offer(new dist(s, 0)); //우선순위큐
        d[s] = 0;
        int cnt = 0;
        while (!Q.isEmpty()) {
            u = Q.poll().index;
            tmp = adjacent[u];
            p = tmp.next;
            while (p != null) {
                for (int k = 0; k < i; k++) {
                    if (p.Name.equals(adjacent[k].Name)) {
                        v = k;
                        break;
                    }
                }
                if (d[v] == -1) {
                    d[v] = d[u] + p.dis; //최단경로길이
                    Q.offer(new dist(v, d[v]));
                    w = 0;
                    while (path[u][w] != null) {
                        path[v][w] = path[u][w]; //경로 누적 저장
                        w++;
                    }
                    path[v][w] = adjacent[u].Name;
                } else if (d[v] > d[u] + p.dis) {
                    d[v] = d[u] + p.dis; //최단경로길이
                    Q.offer(new dist(v, d[v]));
                    w = 0;
                    while (path[u][w] != null) { //경로 누적 저장
                        path[v][w] = path[u][w];
                        w++;
                    }
                    path[v][w] = adjacent[u].Name;
                }
                p = p.next;
            }
        }
        w = 0;
        System.out.println("경로 길이 : " + d[dest]);
        System.out.println("경로 : ");
        while (path[dest][w] != null) {
            System.out.println(path[dest][w]);
            w++;
        }
    }
}

class dist implements Comparable<dist> {
    int index;
    double distance;

    public dist(int index, double distance) {
        this.index = index;
        this.distance = distance;
    }

    @Override
    public int compareTo(dist o) {
        return this.distance >= o.distance ? 1 : -1;
    }
}

