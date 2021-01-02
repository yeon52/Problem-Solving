import java.util.Scanner;

public class prog01_03 {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = sc.nextInt();
		int[] ref = new int[n];
		input(n,ref,0);
		int k = sc.nextInt();
		System.out.println(check_sum(ref,0,k,0,n,1,2));
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
	public static int check_sum(int arr[], int index, int k, int cnt, int n, int i, int j)
	{
		if(arr[index]+arr[i]+arr[j]==k)
		{
			if(index==n-3)
			{
				cnt++;
				return cnt;
			}
			else if(i==n-2)
			{
				index++;
				i=index+1;
				j=i+1;
			}
			i++;
			j=i+1;
			cnt++;
			return check_sum(arr,index,k,cnt,n, i, j);
		}
		else if(index==n-3)
			return cnt;
		
		else if(i==n-2 && j==n-1)
		{
			index++;
			i = index+1;
			j = i+1;
			return check_sum(arr,index,k,cnt,n,i,j);
		}
		else if(j==n-1)
		{
			i++;
			j=i+1;
			return check_sum(arr,index,k,cnt,n,i,j);
		}
		else if(j<n-1)
		{
			j++;
			return check_sum(arr,index,k,cnt,n, i, j);
		}
		return 0;
	}
}
