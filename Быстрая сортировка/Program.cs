int[] arr = { 0, -5, 2, 3, 5, 9, -1, 7 };
int[] res = QuickSort(arr, 0, arr.Length - 1);
Console.Write($"Отсортированный массив: [{string.Join(", ", res)}]");
int[] QuickSort(int[] inputArray, int minIndex, int maxIndex)
{
    if(minIndex >= maxIndex) return inputArray;
    int pivot = GetPivotIndex(inputArray, minIndex, maxIndex);
    QuickSort(inputArray, minIndex, pivot - 1);
    QuickSort(inputArray, pivot + 1, maxIndex);
    return inputArray;
}

int GetPivotIndex(int[] inputArray, int minIndex, int maxIndex)
{
    int pivotIndex = minIndex - 1;
    for(int i = minIndex; i <= maxIndex; i++)
    {
        if (inputArray[i] < inputArray[maxIndex])
        {
            pivotIndex++;
            Swap(ref inputArray[pivotIndex], ref inputArray[i]);
        }
    }
    pivotIndex++;
    Swap(ref inputArray[pivotIndex], ref inputArray[maxIndex]);
    return pivotIndex;
}

void Swap(ref int leftValue, ref int rightValue)
{
    int temp = leftValue;
    leftValue = rightValue;
    rightValue = temp;
}
