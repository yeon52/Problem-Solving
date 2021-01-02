import java.util.Scanner;

public class prog01_04 {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = sc.nextInt();
		int[] ref = new int[n];
		input(n,ref,0);
		int k = sc.nextInt();
		System.out.println(ref[nearest(0,n-1,ref,k)]);
	}
	public static int input(int n, int arr[], int cnt)
	{
		if(cnt<n)
		{
			arr[cnt] = sc.nextInt();
			cnt++;
			input(n,arr,cnt);
		}
		return 0;
	}
	public static int nearest(int begin, int end, int arr[], int k)
	{
		int average = (arr[begin]+arr[end])/2;
		if(begin==end)
			return begin;
		if(k>average)
		{
			begin +=1;
			return nearest(begin,end,arr,k);
		}
		else
		{
			end-=1;
			return nearest(begin,end,arr,k);
		}
	}
}
