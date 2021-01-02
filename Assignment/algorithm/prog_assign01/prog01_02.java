import java.util.Scanner;

public class prog01_02 {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {

		int n = sc.nextInt();
		int[] ref = new int[n];
		input(n,ref,0);
		print_rank(0,n,ref);
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
	public static int print_rank(int index, int n, int arr[])
	{
		if(index<=n-1)
		{
			System.out.print(k_rank(arr,arr[index],n,0,0)+1+" ");
			index++;
			return print_rank(index,n,arr);
		}
		return 0;
	}
}