import java.util.Scanner;

public class prog01_01 {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {

		int n = sc.nextInt();
		int[] ref = new int[n];
		input(n,ref,0);
		int k = sc.nextInt();
		System.out.println(k_rank(ref,k,n,0,0)+1);
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
	public static int k_rank(int arr[], int k, int n, int index, int cnt)
	{
		if(index!=n && arr[index]<k )
		{
			cnt++;
			index++;
			return k_rank(arr,k,n,index,cnt);
			
		}
		else if(index!=n && arr[index]>=k)
		{
			index++;
			return k_rank(arr,k,n,index,cnt);
			
		}
		return cnt;
	}
}
