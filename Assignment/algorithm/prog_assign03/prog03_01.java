import java.util.Arrays;

public class prog03_01 {
    static int N1 = 1000;
    static int N2 = 10000;
    static int N3 = 100000;

    public static void main(String[] args) {
        int[] arr_rand_N1 = new int[N1];//랜덤데이터
        int[] arr_rand_N2 = new int[N2];
        int[] arr_rand_N3 = new int[N3];
        int[] arr_Reverse_N1 = new int[N1];//내림차순데이터
        int[] arr_Reverse_N2 = new int[N2];
        int[] arr_Reverse_N3 = new int[N3];
        long startTime, endTime;
        double sum = 0;
        System.out.printf("\t\t\tRandom1000\t Reverse1000\t Random10000\t Reverse10000\t Random100000\t Reverse100000\n");
        makeReverseArray(arr_Reverse_N1, N1);
        makeReverseArray(arr_Reverse_N2, N2);
        makeReverseArray(arr_Reverse_N3, N3);
        
        //버블정렬
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            sum += bubbleSort(arr_rand_N1, N1);
        }
        double bubble_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            sum += bubbleSort(arr_rand_N2, N2);
        }
        double bubble_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            sum += bubbleSort(arr_rand_N3, N3);
        }
        double bubble_rand_N3 = sum / 10.0;
        sum = 0;
        double bubble_Reverse_N1 = bubbleSort(arr_Reverse_N1, N1);
        double bubble_Reverse_N2 = bubbleSort(arr_Reverse_N2, N2);
        double bubble_Reverse_N3 = bubbleSort(arr_Reverse_N3, N3);
        System.out.printf("Bubble\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",bubble_rand_N1,bubble_Reverse_N1,bubble_rand_N2,bubble_Reverse_N2,bubble_rand_N3,bubble_Reverse_N3);
        
        //선택
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            sum += selectionSort(arr_rand_N1, N1);
        }
        double select_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            sum += selectionSort(arr_rand_N2, N2);
        }
        double select_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            sum += selectionSort(arr_rand_N3, N3);
        }
        double select_rand_N3 = sum / 10.0;
        sum = 0;
        double select_Reverse_N1 = selectionSort(arr_Reverse_N1, N1);
        double select_Reverse_N2 = selectionSort(arr_Reverse_N2, N2);
        double select_Reverse_N3 = selectionSort(arr_Reverse_N3, N3);
        System.out.printf("Selection\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",select_rand_N1,select_Reverse_N1,select_rand_N2,select_Reverse_N2,select_rand_N3,select_Reverse_N3);
       
        //삽입정렬
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            sum += insertionSort(arr_rand_N1, N1);
        }
        double insert_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            sum += insertionSort(arr_rand_N2, N2);
        }
        double insert_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            sum += insertionSort(arr_rand_N3, N3);
        }
        double insert_rand_N3 = sum / 10.0;
        sum = 0;
        double insert_Reverse_N1 = insertionSort(arr_Reverse_N1, N1);
        double insert_Reverse_N2 = insertionSort(arr_Reverse_N2, N2);
        double insert_Reverse_N3 = insertionSort(arr_Reverse_N3, N3);
        System.out.printf("Insertion\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",insert_rand_N1,insert_Reverse_N1,insert_rand_N2,insert_Reverse_N2,insert_rand_N3,insert_Reverse_N3);

        //합병정렬
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            mergeSort(arr_rand_N1, 0, N1-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double merge_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            mergeSort(arr_rand_N2, 0, N2-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double merge_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            mergeSort(arr_rand_N3, 0, N3-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double merge_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        mergeSort(arr_Reverse_N1,0, N1-1);
        endTime = System.currentTimeMillis();
        double merge_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        mergeSort(arr_Reverse_N2,0, N2-1);
        endTime = System.currentTimeMillis();
        double merge_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        mergeSort(arr_Reverse_N3,0, N3-1);
        endTime = System.currentTimeMillis();
        double merge_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Merge\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",merge_rand_N1,merge_Reverse_N1,merge_rand_N2,merge_Reverse_N2,merge_rand_N3,merge_Reverse_N3);

        //빠른정렬1
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            quickSort1(arr_rand_N1, 0, N1-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick1_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            quickSort1(arr_rand_N2, 0, N2-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick1_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            quickSort1(arr_rand_N3, 0, N3-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick1_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        quickSort1(arr_Reverse_N1,0, N1-1);
        endTime = System.currentTimeMillis();
        double quick1_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort1(arr_Reverse_N2,0, N2-1);
        endTime = System.currentTimeMillis();
        double quick1_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort1(arr_Reverse_N3,0, N3-1);
        endTime = System.currentTimeMillis();
        double quick1_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Quick1\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",quick1_rand_N1,quick1_Reverse_N1,quick1_rand_N2,quick1_Reverse_N2,quick1_rand_N3,quick1_Reverse_N3);
      
      //빠른정렬2
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            quickSort2(arr_rand_N1, 0, N1-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick2_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            quickSort2(arr_rand_N2, 0, N2-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick2_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            quickSort2(arr_rand_N3, 0, N3-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick2_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        quickSort2(arr_Reverse_N1,0, N1-1);
        endTime = System.currentTimeMillis();
        double quick2_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort2(arr_Reverse_N2,0, N2-1);
        endTime = System.currentTimeMillis();
        double quick2_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort2(arr_Reverse_N3,0, N3-1);
        endTime = System.currentTimeMillis();
        double quick2_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Quick2\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",quick2_rand_N1,quick2_Reverse_N1,quick2_rand_N2,quick2_Reverse_N2,quick2_rand_N3,quick2_Reverse_N3);

        //빠른정렬 3
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            quickSort3(arr_rand_N1, 0, N1-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick3_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            quickSort3(arr_rand_N2, 0, N2-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick3_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            quickSort3(arr_rand_N3, 0, N3-1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double quick3_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        quickSort3(arr_Reverse_N1,0, N1-1);
        endTime = System.currentTimeMillis();
        double quick3_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort3(arr_Reverse_N2,0, N2-1);
        endTime = System.currentTimeMillis();
        double quick3_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        quickSort3(arr_Reverse_N3,0, N3-1);
        endTime = System.currentTimeMillis();
        double quick3_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Quick3\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",quick3_rand_N1,quick3_Reverse_N1,quick3_rand_N2,quick3_Reverse_N2,quick3_rand_N3,quick3_Reverse_N3);
        
        //힙정렬
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            heapSort(arr_rand_N1,N1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double heap_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            heapSort(arr_rand_N2,N2);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double heap_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            heapSort(arr_rand_N3,N3);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double heap_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        heapSort(arr_Reverse_N1,N1);
        endTime = System.currentTimeMillis();
        double heap_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        heapSort(arr_Reverse_N2,N2);
        endTime = System.currentTimeMillis();
        double heap_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        heapSort(arr_Reverse_N3,N3);
        endTime = System.currentTimeMillis();
        double heap_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Heap\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",heap_rand_N1,heap_Reverse_N1,heap_rand_N2,heap_Reverse_N2,heap_rand_N3,heap_Reverse_N3);

        //라이브러리
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N1, N1);
            startTime = System.currentTimeMillis();
            Arrays.sort(arr_rand_N1);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double library_rand_N1 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N2, N2);
            startTime = System.currentTimeMillis();
            Arrays.sort(arr_rand_N2);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double library_rand_N2 = sum / 10.0;
        sum = 0;
        for (int i = 0; i < 10; i++) {
            makeRandomArray(arr_rand_N3, N3);
            startTime = System.currentTimeMillis();
            Arrays.sort(arr_rand_N3);
            endTime = System.currentTimeMillis();
            sum += (endTime-startTime)/1000.0;
        }
        double library_rand_N3 = sum / 10.0;
        sum = 0;

        startTime = System.currentTimeMillis();
        Arrays.sort(arr_Reverse_N1);
        endTime = System.currentTimeMillis();
        double library_Reverse_N1 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        Arrays.sort(arr_Reverse_N2);
        endTime = System.currentTimeMillis();
        double library_Reverse_N2 = (endTime-startTime)/1000.0;

        startTime = System.currentTimeMillis();
        Arrays.sort(arr_Reverse_N3);
        endTime = System.currentTimeMillis();
        double library_Reverse_N3 = (endTime-startTime)/1000.0;
        System.out.printf("Library\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\t\t\t%.3f\n",library_rand_N1,library_Reverse_N1,library_rand_N2,library_Reverse_N2,library_rand_N3,library_Reverse_N3);
    }

    public static double bubbleSort(int arr[], int N) { //버블정렬
        long startTime = System.currentTimeMillis();
        int tmp = 0;
        while (N > 0) {
            for (int i = 0; i < N - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    tmp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = tmp;
                }
            }
            N--;
        }
        long endTime = System.currentTimeMillis();
        return (endTime - startTime) / 1000.0;
    }

    public static double selectionSort(int arr[], int N) { //선택정렬
        long startTime = System.currentTimeMillis();
        int max, max_index = 0, tmp = 0;
        while (N > 0) {
            max = arr[0];
            for (int i = 0; i < N; i++) {
                if (arr[i] > max) {
                    max = arr[i];
                    max_index = i;
                }
            }
            tmp = arr[max_index];
            arr[max_index] = arr[N - 1];
            arr[N - 1] = tmp;
            N--;
        }
        long endTime = System.currentTimeMillis();
        return (endTime - startTime) / 1000.0;
    }

    public static double insertionSort(int arr[], int N) { //삽입정렬
        long startTime = System.currentTimeMillis();
        int insert = arr[1], insert_index = 1;
        int tmp = 0;
        while (insert_index < N - 1) {
            if (arr[0] > insert) {
                for (int j = 0; j < insert_index; j++) {
                    arr[j + 1] = arr[j];
                }
                arr[0] = insert;
                insert_index++;
                continue;
            }
            for (int i = insert_index; i >= 0; i--) {
                if (arr[i] < insert) {
                    for (int j = insert_index - 1; j >= i; j--) {
                        arr[j + 1] = arr[j];
                    }
                    arr[i + 1] = insert;
                    break;
                }
            }
            insert_index++;
            insert = arr[insert_index];
        }
        long endTime = System.currentTimeMillis();
        return (endTime - startTime) / 1000.0;
    }
    public static void mergeSort(int arr[], int p, int r) { //합병정렬
        int q;
        if (p < r) {
            q = (p + r) / 2;
            mergeSort(arr, p, q);
            mergeSort(arr, q + 1, r);
            merge(arr, p, q, r);
        }
    }

    public static void merge(int arr[], int p, int q, int r) {
        int k = p, i = p, j = q + 1;
        int[] sort = new int[r + 1];
        while (k < r) {
            while (i <= q && j <= r) {
                if (arr[i] <= arr[j])
                    sort[k++] = arr[i++];
                else
                    sort[k++] = arr[j++];
            }
            if (i > q) {
                for (int n = j; n <= r; n++)
                    sort[k++] = arr[n];
            } else {
                for (int n = i; n <= q; n++)
                    sort[k++] = arr[n];
            }
        }
        for (int n = p; n <= r; n++)
            arr[n] = sort[n];
    }

    public static void quickSort1(int arr[], int p, int r) { //빠른정렬 - 마지막값이 피봇
        int q;
        if (p < r) {
            q = partition(arr, p, r);
            quickSort1(arr, p, q - 1);
            quickSort1(arr, q + 1, r);
        }
        long endTime = System.currentTimeMillis();
    }

    public static void quickSort2(int arr[], int p, int r) { //빠른정렬 - 첫번째, 가운데, 마지막 중 중간값 피봇
        int q, tmp;
        if (p - r > 1) {
            for (int n = 0; n < 3; n++) {
                if (arr[p] > arr[(p + r) / 2]) {
                    tmp = arr[p];
                    arr[p] = arr[(p + r) / 2];
                    arr[(p + r) / 2] = tmp;
                }
                if (arr[(p + r) / 2] > arr[r]) {
                    tmp = arr[(p + r) / 2];
                    arr[(p + r) / 2] = arr[r];
                    arr[r] = tmp;
                }
                if (arr[p] > arr[r]) {
                    tmp = arr[p];
                    arr[p] = arr[r];
                    arr[r] = tmp;
                }
            }
            tmp = arr[(p + r) / 2];
            arr[(p + r) / 2] = arr[r];
            arr[r] = tmp;
        }
        if (p < r) {
            q = partition(arr, p, r);
            quickSort2(arr, p, q - 1);
            quickSort2(arr, q + 1, r);
        }
    }

    public static void quickSort3(int arr[], int p, int r) { //빠른정렬 - 랜덤 피봇
        int q;
        if (p < r) {
            q = partition_random(arr, p, r);
            quickSort3(arr, p, q - 1);
            quickSort3(arr, q + 1, r);
        }
    }

    public static int partition(int arr[], int p, int r) {
        int q, tmp, i = p - 1, x = arr[r];
        for (int j = p; j < r; j++) {
            if (arr[j] <= x) {
                i++;
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        tmp = arr[i + 1];
        arr[i + 1] = arr[r];
        arr[r] = tmp;

        return i + 1;
    }

    public static int partition_random(int arr[], int p, int r) {
        int q, tmp, i = p - 1;
        int Random = (int) (Math.random() * (r - p + 1) + p);
        tmp = arr[Random];
        arr[Random] = arr[r];
        arr[r] = tmp;

        int x = arr[r];
        for (int j = p; j < r; j++) {
            if (arr[j] <= x) {
                i++;
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        tmp = arr[i + 1];
        arr[i + 1] = arr[r];
        arr[r] = tmp;

        return i + 1;
    }

    public static void heapSort(int arr[], int N) {
        int tmp;
        for (int i = (N - 1) / 2; i > 0; i--)
            MAX_HEAPIFY(arr, i, N);

        for (int i = N - 1; i > 0; i--) {
            tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
            N--;
            MAX_HEAPIFY(arr, 0, N);
        }
    }

    public static void MAX_HEAPIFY(int arr[], int i, int N) {
        int k, tmp;
        if (2 * i + 1 > N - 1) //자식이 없을 경우
            return;
        if (2 * i + 2 > N - 1 || arr[2 * i + 1] >= arr[2 * i + 2])
            k = 2 * i + 1;
        else
            k = 2 * i + 2;
        if (arr[i] >= arr[k])
            return;
        tmp = arr[i];
        arr[i] = arr[k];
        arr[k] = tmp;
        MAX_HEAPIFY(arr, k, N);
    }

    public static void makeRandomArray(int arr[], int N) {
        for (int i = 0; i < N; i++)
            arr[i] = (int)(Math.random()*N+1);
    }

    public static void makeReverseArray(int arr[], int N) {
        for (int i = 0; i < N; i++)
            arr[i] = N - i;
    }
}

