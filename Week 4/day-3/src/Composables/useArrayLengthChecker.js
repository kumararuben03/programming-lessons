const useArrayLengthChecker = (dataArray) => {
  const arrayLength = ref(0);
  const showAlert = ref(false);

  watch(
    dataArray,
    (newArray) => {
      arrayLength.value = newArray.length;
      showAlert.value = newArray.length === 0;
    },
    { immediate: true }
  );

  onMounted(() => {
    displayResults();
  });

  const displayResults = () => {
    const resultContainer = document.getElementById("results");
    if (resultContainer) {
      resultContainer.innerHTML = `${
        showAlert.value
          ? '<p style="color:red;">The array is currently empty.</p>'
          : ""
      } <p>Array length: ${arrayLength.value}</p>`;
    }
  };

  watch([arrayLength, showAlert], () => {
    displayResults();
  });

  return {};
};

export default useArrayLengthChecker;
