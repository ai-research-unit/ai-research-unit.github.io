
# __The Euler Product Operator__

## Introduction

The Euler product is usually written as a formula for an $L$-function, as an infinite product over the primes equal to a Dirichlet series. This article reads the same construction as an **operator**: the map that takes a system of local factors, one at each prime, and assembles them into a single global arithmetic function. Written in this form the Euler product becomes a structural isomorphism between the algebra of arithmetic functions and the restricted product of its $p$-primary components, and the convergence of the product becomes the statement that this isomorphism is an isometry in the appropriate norm. The operator language also makes the two hypotheses visible: multiplicativity is what allows the assembly at all, and the growth of the local coefficients is what decides convergence.

The conventions are those of the category. The algebra of arithmetic functions under Dirichlet convolution is $\mathcal{A}$; the $p$-primary component is $\mathcal{A}_p=\{f:\operatorname{supp}f\subseteq p^{\mathbb{N}}\}$; the form of the category is $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$ on $\mathcal{H}=\ell^2$; the local factor of an $L$-function at $p$ is $L_p(f,s)=\sum_{r\ge0}f(p^r)p^{-rs}$. The companion articles are *Multiplication Operators on an L-Function* for the operator $M_h$ and *The Shift Operator on the Coefficients* for the local shifts. Nothing here reads a distance as an object; convergence is the convergence of the product in the norm of the operators on $\mathcal{H}$.

## The Local Components

### The $p$-primary component as an algebra

**Proposition.** For each prime $p$ the set $\mathcal{A}_p$ is a subalgebra of $\mathcal{A}$, isomorphic to the algebra of formal power series $\mathbb{C}[[X]]$ under
$$
\mathcal{A}_p\to\mathbb{C}[[X]],\qquad f\mapsto \sum_{r\ge0}f(p^r)X^r,
$$
which carries the Cauchy product of sequences to the product of power series. The local factor $L_p(f,s)$ is the value at $X=p^{-s}$ of the image of $f$.

**Proof.** If $f,g$ are supported on $p$-powers then so is $f*g$, and $(f*g)(p^r)=\sum_{j=0}^rf(p^j)g(p^{r-j})$ is the Cauchy product. The identity $\varepsilon$ corresponds to $1$, and the display is the geometric substitution.

**Corollary.** The unit group of $\mathcal{A}_p$ is $\{f:f(p^0)=f(1)\ne0\}$, and $\mathcal{A}_p$ has no zero divisors.

### The restricted product

**Definition.** The **restricted product** $\bigoplus'_p\mathcal{A}_p$ is the set of tuples $(f_p)_p$ with $f_p\in\mathcal{A}_p$ and $f_p=\varepsilon$ for all but finitely many $p$, with componentwise convolution. It is a nonunital algebra without identity, and it carries the direct-sum topology.

**Theorem (the local decomposition).** The map
$$
E:\bigoplus\nolimits'_p\mathcal{A}_p\to\mathcal{A},\qquad E((f_p)_p)(n)=\prod_{p^r\parallel n}f_p(p^r),
$$
is an isomorphism of algebras, and it is the **Euler product operator**. Its inverse is the factorisation $f\mapsto(f_p)_p$ with $f_p(p^r)=f(p^r)$. In particular every multiplicative function is $E$ of its local data, and $E$ is multiplicative: $E((f_p)*(g_p))=E((f_p))\, E((g_p))$.

**Proof.** The product in the display is finite because $n$ has finitely many prime factors, and if all but finitely many $f_p$ equal $\varepsilon$ then $E((f_p))$ is supported on the finitely many affected primes, so $E$ is well defined. For multiplicativity, expand both sides at $n=\prod p^{r_p}$: the left side is the convolution of two functions each of which is multiplicative, hence multiplicative, and at $n$ it equals the product of the local convolutions, which is the right side. Injectivity and surjectivity are the unique factorisation of $n$ read coefficientwise.

**Remark (the reading of the Euler product).** With the operator $E$ the Euler product of the $L$-function is the identity
$$
L(E((f_p)),s)=\prod_pL_p(f_p,s),
$$
so the Euler product is not an equality to be proved at each $s$ but the definition of the $L$-function on the image of $E$; the analytic content is the convergence of the right side, which is the next section.

## Convergence of the Operator Product

### Absolute convergence

**Theorem (Euler).** Let $f$ be multiplicative with $|f(n)|\le Cn^{\sigma_0}$ for some $C>0$ and real $\sigma_0$. Then the Euler product
$$
\prod_pL_p(f,s)=\prod_p\Bigl(\sum_{r\ge0}f(p^r)p^{-rs}\Bigr)
$$
converges absolutely and locally uniformly in $\Re s>\sigma_0+1$, and its value is $L(f,s)=\sum_nf(n)n^{-s}$. The product converges conditionally for $\Re s>\sigma_0$ in the cases where the local sums stay bounded away from $0$.

**Proof.** The estimate $|f(p^r)|\le Cp^{r\sigma_0}$ gives $\sum_{r\ge0}|f(p^r)|p^{-r\Re s}\le C(1-p^{\sigma_0-\Re s})^{-1}$, so $\sum_p|L_p(f,s)-1|\le C\sum_pp^{\sigma_0-\Re s}$, which converges when $\Re s>\sigma_0+1$. For the value, expand the finite product over $p\le P$ and compare with the Dirichlet series: the two differ by the terms divisible by a prime $>P$, whose total is $O(\sum_{n>P}|f(n)|n^{-\Re s})$, tending to $0$. This is the classical Euler product of *Analytic Number Theory*.

**Corollary (convergence in operator norm).** If additionally $f_p-\delta_1$ is summable in $\ell^1$ over $p$, the operator product $\prod_pM_{f_p}$ converges in the norm of $\mathcal{L}(\mathcal{H})$ to $M_f$, and $\|M_f\|\le\prod_p\|M_{f_p}\|$.

**Proof.** Apply the telescoping estimate of *Multiplication Operators on an L-Function* to the local multiplication operators; the summability hypothesis is exactly the hypothesis of that estimate.

### The local factor as an operator

**Proposition.** On the $p$-primary component the multiplication by $f_p$ is the Toeplitz operator of the sequence $(f_p(p^r))_r$, and the Euler product operator $E$ on the level of $L$-functions corresponds to the identification
$$
\mathcal{L}\Bigl(\bigoplus\nolimits'_p\mathcal{A}_p\Bigr)\;\cong\;\bigotimes\nolimits_p\mathcal{L}(\mathcal{A}_p)
$$
of operator algebras, under which $\prod_pM_{f_p}$ goes to the tensor product of the local operators.

**Proof.** The identification is the associativity of the direct sum and the commutativity of operators supported on disjoint prime sets; the tensor statement follows from the multiplicativity of $E$ and the fact that the local operators act on independent coordinates.

## Action on the Coefficients

### The coefficient formula

**Theorem.** For $f=E((f_p)_p)$ multiplicative and $n=\prod_{i=1}^kp_i^{r_i}$,
$$
f(n)=\prod_{i=1}^kf_{p_i}(p_i^{r_i}),\qquad f(1)=1,
$$
and the Dirichlet series of $f$ is the absolutely convergent product. Conversely, if $L(f,s)=\prod_pG_p(s)$ with each $G_p$ a power series in $p^{-s}$ with constant term $1$ and the product absolutely convergent in a half-plane, then $f$ is multiplicative and $G_p=L_p(f,\cdot)$.

**Proof.** The first statement is the definition of $E$. For the converse, expand the product in the half-plane of absolute convergence: termwise expansion is legitimate there, the coefficient of $n^{-s}$ receives contributions from the choices of local exponents summing to $n$'s factorisation, and it equals $\prod f_{p_i}(p_i^{r_i})$ with $f_{p_i}$ the coefficients of $G_{p_i}$; this forces $f$ to be the $E$ of those local functions, hence multiplicative.

### Examples

**Example (the zeta factor).** For $f=\mathbf{1}$ the constant function, $f_p=1$ on all $p$-powers and $L_p(f,s)=(1-p^{-s})^{-1}$; the Euler product is $\prod_p(1-p^{-s})^{-1}=\zeta(s)$ for $\Re s>1$. The operator is $M_{\mathbf 1}$, the divisor-sum operator of *Multiplication Operators on an L-Function*.

**Example (a character).** For a Dirichlet character $\chi$, $f=\chi$ is completely multiplicative, $f_p(p^r)=\chi(p)^r$, and $L_p=(1-\chi(p)p^{-s})^{-1}$; the product is $L(\chi,s)$, convergent for $\Re s>1$.

**Example (a cusp form).** For a normalised Hecke eigenform, $f(n)=a_n$ is multiplicative, the local factor is $(1-a_pp^{-s}+\varepsilon(p)p^{k-1-2s})^{-1}$, and the product is the degree-two $L$-function of *The Hecke Operator*.

## Failure of the Degenerate Cases

The Euler product operator $E$ requires multiplicativity, and it fails to be defined in three degenerate ways. First, for a nonmultiplicative $f$ the factorisation $f(n)=\prod f_{p_i}(p_i^{r_i})$ is false, so $f$ is not $E$ of any tuple; the Dirichlet series of $f$ then has no Euler product, even though it may converge. Second, the product may fail to converge absolutely while the Dirichlet series converges: if $f$ is multiplicative with $|f(n)|\le Cn^{\sigma_0}$, the Euler product converges absolutely only in $\Re s>\sigma_0+1$, while the Dirichlet series may converge in a wider half-plane, and the operator product $\prod_pM_{f_p}$ then fails to converge in norm although each factor is bounded. Third, the local factors may vanish: if some $L_p(f,s_0)=0$, the Euler product vanishes at $s_0$ although the Dirichlet series may not; a zero of a local factor at the boundary of the half-plane of absolute convergence is the degenerate case in which the product converges to $0$ and the Dirichlet series does not. All three failures are contained in the estimate of the convergence theorem, where the hypothesis $\Re s>\sigma_0+1$ is exactly what excludes the boundary.

## Summary

The Euler product operator $E$ sends a tuple of local functions $(f_p)_p$, almost all equal to $\varepsilon$, to the multiplicative function $E((f_p))(n)=\prod_{p^r\parallel n}f_p(p^r)$, and it is an isomorphism from the restricted product $\bigoplus'_p\mathcal{A}_p$ to the algebra $\mathcal{A}$; the local component $\mathcal{A}_p$ is the algebra of formal power series in one variable, and the local factor $L_p$ is its evaluation at $p^{-s}$. The Euler product of an $L$-function is the identity $L(E((f_p)),s)=\prod_pL_p(f_p,s)$, and its convergence is governed by the growth of the local coefficients: for multiplicative $f$ with $|f(n)|\le Cn^{\sigma_0}$ the product converges absolutely and locally uniformly in $\Re s>\sigma_0+1$ and equals $\sum_nf(n)n^{-s}$, and when the local perturbations are summable in $\ell^1$ the operator product $\prod_pM_{f_p}$ converges in norm to $M_f$ and makes $M_f$ a compact perturbation of the identity. The degenerate failures are the absence of multiplicativity, the slower convergence of the product than of the series, and the vanishing of a local factor at the boundary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A}_p=\{f:\operatorname{supp}f\subseteq p^{\mathbb{N}}\}$ | $p$-primary component |
| $\bigoplus'_p\mathcal{A}_p$ | Restricted product of the local algebras |
| $E((f_p)_p)(n)=\prod_{p^r\parallel n}f_p(p^r)$ | Euler product operator |
| $L_p(f,s)=\sum_{r\ge0}f(p^r)p^{-rs}$ | Local factor |
| $L(E((f_p)),s)=\prod_pL_p(f_p,s)$ | Euler product identity |
| $\|f(n)\|\le Cn^{\sigma_0}$ | Growth hypothesis for absolute convergence |
| $\prod_pM_{f_p}$ | Euler product as an operator product |
| $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ | The zeta factor, $f=\mathbf{1}$ |
| $(1-a_pp^{-s}+\varepsilon(p)p^{k-1-2s})^{-1}$ | Local factor of a Hecke eigenform |

## Further Reading

- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the Euler product and the convergence of the local factors.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the Euler product of a general $L$-function.
- Paul Garrett, *Basic Structures of Function Field Arithmetic* (Springer, 1996), for the restricted product of local algebras and the adelic Euler product.
- Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory* (American Mathematical Society, 2015), for the growth hypotheses on multiplicative functions.
- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (thesis, Princeton, 1950; reprinted in *Algebraic Number Theory*), for the local-global factorization of $L$-functions.
