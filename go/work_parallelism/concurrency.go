package main

import (
	"crypto/sha256"
	"runtime"
	"sync"
)

func cpuWork() {
	data := []byte("benchmark")
	for i := 0; i < 10_000_000; i++ {
		sha256.Sum256(data)
	}
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var wg sync.WaitGroup
	cores := runtime.NumCPU()

	for i := 0; i < cores; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()
			cpuWork()
		}()
	}
	wg.Wait()
}
