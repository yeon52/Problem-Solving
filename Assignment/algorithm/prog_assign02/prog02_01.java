import java.util.Scanner;

public class prog02_01 {
    static Scanner sc = new Scanner(System.in);
    static int PATHWAY_COLOUR = 0;
    static int WALL_COLOUR = 1;
    static int BLOCKED_COLOUR = 2;
    static int PATH_COLOUR = 3;
    static int cnt = 0;
    static int K, N;
    static int[][] maze;
    public static void main(final String[] args) {
        N = sc.nextInt();
        maze = new int[N][N];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                maze[i][j] = sc.nextInt();
            }
        }
        K = sc.nextInt();
        findMazePath(0,0,0);
        System.out.println(cnt);
    }
    public static int findMazePath(final int x, final int y, final int dist)
    {
        if(x<0 || y<0||x>=N||y>=N||maze[y][x]!=PATHWAY_COLOUR)
            return 0;
        if(x==N-1 && y==N-1)
        {
            maze[y][x] = PATH_COLOUR;
            if(dist<=K)
                cnt++;
        }
        else {
            maze[y][x] = PATH_COLOUR;
            findMazePath(x - 1, y, dist+1);
            findMazePath(x, y + 1, dist+1);
            findMazePath(x + 1, y, dist+1);
            findMazePath(x, y - 1, dist+1);
        }
            maze[y][x] = 0;
            return 0;
        }
}
