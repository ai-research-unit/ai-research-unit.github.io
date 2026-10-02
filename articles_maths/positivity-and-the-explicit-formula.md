
# __Positivity and the Explicit Formula__

## Introduction

The explicit formula of Weil is an identity that relates the zeros of a completed $L$-function, its archimedean factor and its prime coefficients to a test function on the critical line. Its importance is that it turns a statement about the location of the zeros into a statement about the positive definiteness of a Hermitian form: the Riemann hypothesis is equivalent to the positivity of the Weil distribution evaluated on the convolution squares of the test functions. This article states the explicit formula, defines the Weil distribution, proves that it is Hermitian, and formulates the positivity criterion. It is the analytical heart of the `* Theory` group: the involution of the zeros is *The Conjugate Symmetry and the Critical Line*, the Hermitian form is *Hermitian Forms and the Zeta Function*, and the operator side is in *Hermitian Dirichlet Forms* and *Spectral Theory*.

The conventions are those of the category. $\Lambda_f$ is the completed $L$-function of *The Functional Equation and the Conjugate Symmetry of an L-Function*, the test function $h$ is in the space of functions whose Fourier transforms are compactly supported and which are holomorphic in a strip, and the involution on the test functions is $h^*(x)=\overline{h(-x)}$, so that $\widehat{h^*}=\overline{\widehat h}$ on the real line. Nothing here reads a distance as an object; the Fourier transform is a normalisation and the positivity is the positivity of a Hermitian form on a space of test functions.

## The Explicit Formula

### Statement

**Theorem (the explicit formula).** For a test function $h$ as above,
$$
\sum_{\rho}\widehat h(\rho)=\widehat h(1)+\widehat h(0)-\sum_{j}\widehat h(-\mu_j)+\frac{1}{2\pi}\int_{-\infty}^{\infty}\widehat h(r)\,\frac{\gamma_\infty'}{\gamma_\infty}\Bigl(\tfrac12+ir\Bigr)\,dr+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\bigl(g(\log n)+g(-\log n)\bigr),
$$
where the sum is over the nontrivial zeros $\rho$ of $\Lambda_f$ with multiplicity, the archimedean term is the logarithmic derivative of the gamma factor, the function $g$ is the inverse Fourier transform of $\widehat h$, and $\Lambda$ is the von Mangoldt function; the sum over the zeros converges when $h$ is smooth and compactly supported in the appropriate sense.

**Proof.** The formula is the residue theorem applied to the logarithmic derivative of $\Lambda_f$ multiplied by $\widehat h$, on a large rectangle; the residues at the zeros give the left side, the residues at the poles give the two terms $\widehat h(1)+\widehat h(0)$, the archimedean term is the cut contribution of the gamma factor, and the prime terms come from the logarithmic derivative of the Euler product, expanded as the series $\sum_{p,k}(\log p)p^{-ks}$. This is the classical explicit formula of *Riemann's Zeta Function* and *Prime Numbers*.

### The Weil distribution

**Definition.** The **Weil distribution** is the functional
$$
W(h)=\sum_{\rho}\widehat h(\rho)\;-\;\widehat h(1)-\widehat h(0)+\sum_{j}\widehat h(-\mu_j)-\frac{1}{2\pi}\int_{-\infty}^{\infty}\widehat h(r)\frac{\gamma_\infty'}{\gamma_\infty}\Bigl(\tfrac12+ir\Bigr)dr ,
$$
so that the explicit formula reads $W(h)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(g(\log n)+g(-\log n))$.

**Theorem.** The Weil distribution is Hermitian,
$$
W(h^*)=\overline{W(h)} ,
$$
and it is a tempered distribution on the space of test functions.

**Proof.** The zeros are symmetric under the conjugation for real coefficients, so the sum $\sum_\rho\widehat h(\rho)$ satisfies the same identity with the conjugate; the prime side is real when $h$ is real and satisfies the Hermitian identity term by term, since $g_{h^*}(x)=\overline{g_h(-x)}$. The temperedness is the growth of the test space; the details are in *Explicit Formulas*.

## Positivity

### The convolution square

**Definition.** The **convolution square** of $h$ is $h*h^*$, whose Fourier transform is $|\widehat h|^2\ge0$ on the real line.

**Theorem (the positivity criterion).** The following are equivalent.
$$
\text{the Riemann hypothesis for } L(f,\cdot),\qquad W(h*h^*)\ge0\ \text{ for every test function }h .
$$
Moreover, $W(h*h^*)\ge0$ for all $h$ is equivalent to the positive definiteness of the Hermitian form $(h_1,h_2)\mapsto W(h_1*h_2^*)$ on the test space.

**Proof.** The explicit formula expresses $W(h*h^*)$ as a sum over the zeros of $|\widehat h(\rho)|^2$ plus the archimedean and prime corrections; the archimedean and prime corrections are the same for all $h$ and depend only on the completion. If all the zeros have real part $1/2$, each $\rho=\frac12+it$ contributes $|\widehat h(\frac12+it)|^2\ge0$ and the total is a sum of nonnegative terms plus a nonnegative archimedean term, so $W(h*h^*)\ge0$. Conversely, if some zero has real part $\beta\ne1/2$, one chooses a test function concentrated near that zero so that the corresponding term dominates and $W(h*h^*)<0$; this is the standard argument of Weil, in *Explicit Formulas*. The equivalence with positive definiteness is the polarisation identity for the Hermitian form $W(h_1*h_2^*)$.

**Corollary.** The positivity criterion gives, without assuming the Riemann hypothesis, the nonnegativity of the form on the subspace of test functions $h$ whose Fourier transform vanishes on the zeros found by computation up to height $T$; hence every numerical verification of the hypothesis is a finite restriction of the positivity.

## Worked Examples

**Example (the pole term).** The term $\widehat h(1)+\widehat h(0)$ is the contribution of the pole of $\zeta$ at $s=1$ and the pole of the completion at $s=0$; it is the source of the prime number theorem, which follows from the explicit formula by choosing $h$ with $\widehat h$ supported near the real axis and separating the pole contribution.

**Example (the trivial zeros).** The term $\sum_j\widehat h(-\mu_j)$ is the contribution of the archimedean places; for $\zeta$ it is $\widehat h$ at the negative even integers, and for a general $L$-function it is the sum over the archimedean parameters.

**Example (the prime side).** The prime side $\sum_n\frac{\Lambda(n)}{\sqrt n}(g(\log n)+g(-\log n))$ is the arithmetic input; it is the reason the explicit formula is a relation between the zeros and the primes, and the positivity of its combination with the archimedean term is the content of the criterion.

## Failure of the Degenerate Cases

The positivity criterion fails in four degenerate configurations. First, the test space must be restricted so that the sum over the zeros converges and the Fourier transform has the required support; on the full space of smooth compactly supported functions the sums need not converge absolutely. Second, the archimedean term is not positive in general, and for a completion with a large archimedean conductor the positivity of $W(h*h^*)$ requires the prime terms to compensate; the criterion is not a term-by-term statement. Third, the trivial zeros and the pole terms are not part of the Hermitian form in the same way as the nontrivial zeros, and the naive statement "$W(h*h^*)\ge0$ iff all zeros have real part $1/2$" must be read with the trivial zeros assigned to the archimedean correction. Fourth, when the $L$-function has a pole in the critical strip the explicit formula has additional residue terms, and the positivity criterion must be modified by the contribution of the pole. These are the boundary cases of the criterion.

## Summary

The explicit formula of Weil expresses the sum of a test function over the nontrivial zeros of a completed $L$-function as the pole terms plus the archimedean term plus the prime terms, and it defines the Weil distribution $W$, a Hermitian tempered distribution. The Riemann hypothesis for $L(f,\cdot)$ is equivalent to the positivity $W(h*h^*)\ge0$ for every test function $h$, equivalently to the positive definiteness of the Hermitian form $(h_1,h_2)\mapsto W(h_1*h_2^*)$. The pole term gives the prime number theorem, the archimedean term is the contribution of the trivial zeros, and the prime side is the arithmetic input. The degenerate cases are the restriction of the test space, the non-positivity of the archimedean term, the treatment of the trivial zeros and the poles inside the critical strip.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$, $\widehat h$, $g$ | Test function, its Fourier transform, its inverse transform |
| $h^*(x)=\overline{h(-x)}$ | The involution on the test functions |
| $\Lambda(n)$ | Von Mangoldt function |
| $\mu_j$ | Archimedean parameters |
| $W(h)$ | Weil distribution |
| $W(h^*)=\overline{W(h)}$ | Hermitian property |
| $h*h^*$, $\widehat{h*h^*}=|\widehat h|^2$ | Convolution square |
| $W(h*h^*)\ge0$ | Positivity criterion |
| $(h_1,h_2)\mapsto W(h_1*h_2^*)$ | Hermitian form |

## Further Reading

- André Weil, *Sur les "formules explicites" de la théorie des nombres premiers* (Meddelanden Lunds Universitets Matematiska Seminarium, 1952), for the original explicit formula and the positivity.
- Harold Edwards, *Riemann's Zeta Function* (Academic Press, 1974), for the explicit formula for the zeta function.
- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the applications to the prime number theorem.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the modern form of the explicit formula.
- Enrico Bombieri, *Problems of the Millennium: The Riemann Hypothesis* (Clay Mathematics Institute, 2000), for the positivity criterion and its history.
