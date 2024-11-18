#include <iostream>
using namespace std;

int interpolationSearch(int arr[], int n, int x) {
    int low = 0, high = n - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) 
	{
        int mid = low + ((x - arr[low]) * (high - low)) / (arr[high] - arr[low]);
        if (arr[mid] == x)
            return mid;
        if (arr[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

int main() {
    int n;
    cout<<"Moi ban nhap so luong phan tu: ";
	cin>>n; 
    int arr[n];
    for(int i=0;i<n;i++)
    {
    	cout<<"Nhap vi tri mang thu "<<i+1<<": ";
    	cin>>arr[i];
	}

    int x;
    cout << "Nhap gia tri can tim: ";
    cin >> x;

    int result = interpolationSearch(arr, n, x);

    if (result != -1)
        cout << "Gia tri " << x << " duoc tim thay tai vi tri " << result << ".\n";
    else
        cout << "Gia tri " << x << " khong ton tai trong mang.\n";

    return 0;
}

