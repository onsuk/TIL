function fakeGenerator() {

    const values = [5, 7, 11];
    let currentIndex = 0;

    return {
        next: function(){
            const iteration = {
                value: values[currentIndex],
                done: (currentIndex === values.length -1)
            }
            currentIndex++;
            return iteration;
        }
    }
}

const iterator = fakeGenerator();

const firstIteration = iterator.next();
const secondIteration = iterator.next();
const thirdIteration = iterator.next();

firstIteration
secondIteration
thirdIteration