import java.util.Scanner;

public class prog02_02 {
    static Scanner sc = new Scanner(System.in);
    static int chk = 0,N;
    static int[][] maze;
    public static void main(String[] args) {
        N = sc.nextInt();
        maze = new int[N][N];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                maze[i][j] = sc.nextInt();
            }
        }
        if(findMazePath(0,0)==1)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
    public static int findMazePath(int x, int y)
    {
        if(x==N-1 && y==N-1)
            return 1;
        else if(x==N-1 || y==N-1)
        {
            if(x==N-1)
            {
                if(maze[y+1][x]==1)
                    return 0;
                chk = 1;
                return findMazePath(x,y+1);
            }
            else {
                if(maze[y][x+1]==1)
                    return 0;
                chk = 0;
                return findMazePath(x + 1, y);
            }
        }
        if(chk == 0)
        {
            if(maze[y][x+1]==1)
            {
                chk = 1;
                if(maze[y+1][x]==1) {
                    chk = 2;
                    return findMazePath(x, y - 1);
                }
                else
                    return findMazePath(x,y+1);
            }
            else
                return findMazePath(x+1,y);
        }
        else if(chk == 1)
        {
            if(maze[y+1][x]==1)
            {
                chk = 0;
                return findMazePath(x+1,y);
            }
            else
                return findMazePath(x,y+1);
        }
        else if(chk == 2)
        {
            if(maze[y-1][x]==1)
            {
                chk = 0;
                return findMazePath(x+1,y);
            }
        }
        return 0;
    }
}
