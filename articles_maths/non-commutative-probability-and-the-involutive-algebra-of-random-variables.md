
# __Non-Commutative Probability and the Involutive Algebra of Random Variables__

## Introduction

The algebra of random variables is commutative, and the commutativity is what makes the classical probability theory: it is the hypothesis under which the product of two random variables is a random variable in the naive sense, under which the joint law of a family is a measure on a product, and under which the conditional expectations are the projections of a lattice of $\sigma$-algebras. **Non-commutative probability** keeps the two structures that do not need the commutativity — an involution $x\mapsto x^*$ on the elements and a state $\varphi$ on the algebra — and drops the product's commutativity:
$$
\varphi(x^*x)\ge0,\qquad \varphi(1)=1 .
$$
The elements are then called random variables, the self-adjoint ones $x=x^*$ are the real random variables, the state is the expectation, and the involution is the conjugation; the pair $(\mathcal{A},\varphi)$ is a **non-commutative probability space**. The theory is the operator-algebraic probability of von Neumann, and its distinctive notion is **freeness**, the independence of the free product, whose central limit is the semicircle law and whose cumulants add. This article develops the involutive algebra with a state, the Gelfand–Naimark–Segal form $\langle x,y\rangle=\varphi(xy^*)$, the distribution of a self-adjoint element, freeness and the free product, the free central limit theorem with the semicircle law and the Catalan moments, and the free cumulants with the $R$-transform.

The classical theory is the commutative case and is fixed elsewhere. The commutative algebra of random variables, its complex conjugation and its real random variables are *The Involution on the Algebra of Random Variables*, later in this category; the covariance form $\varphi(xy^*)$ and its positivity are *The Covariance Function and Hermitian Positivity*, later in this category; the characteristic function and its conjugate symmetry are *The Characteristic Function and Conjugate Symmetry*, later in this category. The states, the positive functionals, the GNS construction, the von Neumann algebras and the spectral theorem are *Operator Algebras*, written, and its companions; the measure-theoretic probability, the independence and the conditional expectation are *Measure-Theoretic Probability* and *Independence and Conditional Expectation*, written, and they supply the classical model in which the algebra is $L^\infty$ and the state is the expectation. No physics is invoked.

Throughout, $\mathcal{A}$ is a unital algebra over $\mathbb{C}$ with an involution $x\mapsto x^*$ and a state $\varphi$: a linear functional with $\varphi(1)=1$ and $\varphi(x^*x)\ge0$ for all $x$; the state is **faithful** when $\varphi(x^*x)=0$ implies $x=0$. The elements are the random variables, the self-adjoint elements $x=x^*$ the real ones. The GNS space is $\mathcal{H}=L^2(\mathcal{A},\varphi)$, the completion of $\mathcal{A}$ in the form $\langle x,y\rangle=\varphi(xy^*)$, with $\|x\|_2=\langle x,x\rangle^{1/2}$, and $\pi$ is the representation of $\mathcal{A}$ on $\mathcal{H}$ by the left multiplication.

## The Involutive Algebra with a State

### Definition

**Definition.** A **non-commutative probability space** is a pair $(\mathcal{A},\varphi)$ of a unital involutive algebra $\mathcal{A}$ and a state $\varphi$. Its elements are called random variables; the **distribution** of a self-adjoint element $x$ is the positive measure $\mu_x$ on $\mathbb{R}$ with
$$
\varphi(x^n)=\int_{\mathbb{R}}t^n\,d\mu_x(t)\qquad(n\ge0),
$$
whose existence is the spectral theorem for the self-adjoint $x$ acting on the GNS space.

**Theorem (the state and the form).** The form
$$
\langle x,y\rangle=\varphi(xy^*)
$$
is linear in the first argument and conjugate-linear in the second, and positive semi-definite, $\langle x,x\rangle=\varphi(x^*x)\ge0$; it is positive definite exactly when the state is faithful. The involution is an anti-linear anti-automorphism, isometric for the form,
$$
(xy)^*=y^*x^*,\qquad (x^*)^*=x,\qquad \langle x^*,y^*\rangle=\overline{\langle y,x\rangle},
$$
and the left multiplication $\pi(a)x=ax$ satisfies $\pi(a)^*=\pi(a^*)$ on the GNS space.

*Proof.* The sesquilinearity is the linearity of $\varphi$ and the anti-linearity of the involution; the positivity is the positivity of the state; the identities are those of an involution, and the adjoint identity is $\langle ax,y\rangle=\varphi(axy^*)=\varphi(x(y^*a^*))=\varphi(x(a^*y)^*)=\langle x,a^*y\rangle$. The GNS construction and the representation are *Operator Algebras*. This is the non-commutative form of the expectation form of the commutative category, and it has the same invariance: the involution on the elements and the adjoint on the left multiplications agree, $\pi(a)^*=\pi(a^*)$.

### Self-adjoint elements and the reality of the state

**Theorem (the real and the imaginary parts).** Every $x$ decomposes as $x=a+ib$ with $a,b$ self-adjoint, $a=\frac12(x+x^*)$, $b=\frac{1}{2i}(x-x^*)$, and the decomposition is unique. The state is real on the self-adjoint elements, $\varphi(x)=\overline{\varphi(x)}$ for $x=x^*$, and the state is self-adjoint, $\varphi(x^*)=\overline{\varphi(x)}$, in general.

*Proof.* The decomposition is the definition of $a,b$ and the uniqueness is the direct sum $\mathcal{A}=\mathcal{A}_{sa}\oplus i\mathcal{A}_{sa}$; the self-adjointness of the state is $\varphi(x^*)=\overline{\varphi(x)}$ for every $x$, which for a self-adjoint $x$ says that $\varphi(x)$ is real. The correspondence with the real random variables of the commutative case is *The Involution on the Algebra of Random Variables*, later in this category.

### The distribution of a self-adjoint element

**Theorem (the moments determine the law).** Let $x$ be self-adjoint and bounded. Then the moments $m_n=\varphi(x^n)$ are real, $m_{2n}\ge0$ and the Hankel matrices $(m_{i+j})_{0\le i,j\le n}$ are positive semi-definite; when the moments satisfy Carleman's condition they determine a unique measure on $\mathbb{R}$, the distribution $\mu_x$ of $x$.

*Proof.* The reality of the moments is the self-adjointness of the state, $m_n=\varphi(x^n)=\overline{\varphi((x^n)^*)}=\overline{m_n}$; the positivity of the Hankel matrices is $\sum_{i,j}c_ic_jm_{i+j}=\varphi\bigl(|\sum_ic_ix^i|^2\bigr)\ge0$; the determinacy is the classical moment theorem. The measure is the spectral measure of $x$ in the GNS representation.

## Free Independence

### Definition

**Definition.** The subalgebras $\mathcal{A}_1,\dots,\mathcal{A}_n$ of $\mathcal{A}$ are **free** (freely independent) if
$$
\varphi(a_1\cdots a_m)=0
$$
whenever the $a_k$ have $\varphi(a_k)=0$ and adjacent $a_k$ lie in distinct subalgebras; the random variables $x_1,\dots,x_n$ are free when the subalgebras they generate are free. The definition is the free analogue of the independence of the classical theory, where the corresponding factorisation is $\mathbb E[\prod X_k]=\prod\mathbb E[X_k]$.

**Theorem (the moments factor under freeness).** If $x_1,\dots,x_n$ are free, then the joint moments $\varphi(x_{i_1}\cdots x_{i_m})$ are determined by the moments of the individual $x_i$ by the recursion that removes the consecutive equal blocks and applies the freeness; in particular for free $x,y$,
$$
\varphi(xy)=\varphi(x)\varphi(y),\qquad \varphi(xyxy)=\varphi(x^2)\varphi(y)^2+\varphi(x)^2\varphi(y^2)-\varphi(x)^2\varphi(y)^2 .
$$

*Proof.* Both sides are the value of the recursion on the mixed moment; the displayed identities are the first two cases, the second obtained by writing each of $x-\varphi(x)$ and $y-\varphi(y)$ and expanding the vanishing of the four-term free moment.

### The free product

**Theorem (the reduced free product).** Let $(\mathcal{A}_i,\varphi_i)$ be non-commutative probability spaces with the states faithful, and let $\mathcal{A}_i^\circ=\ker\varphi_i$. There is a unique pair $(\mathcal{A},\varphi)$, called the **reduced free product** $\mathcal{A}=*_i\mathcal{A}_i$ with $\varphi=*_i\varphi_i$, with $\mathcal{A}$ generated by the $\mathcal{A}_i$ as subalgebras, the $\mathcal{A}_i$ free, $\varphi|_{\mathcal{A}_i}=\varphi_i$, and the GNS space $\mathcal{H}=\bigoplus$ of the alternating tensor products of the $\mathcal{H}_i^\circ$.

*Proof.* The construction is the free product of the algebras with the states determined by the freeness recursion on the alternating words in the $\mathcal{A}_i^\circ$; the uniqueness is the uniqueness of the moments under the recursion. The details are the free product of the operator algebras, *Operator Algebras*.

### The relation to classical independence

**Theorem (the tensor product).** If the states are the expectations on commutative algebras, the algebra generated by independent copies in the classical theory is the tensor product $\bigotimes_i\mathcal{A}_i$ with the product state $\otimes_i\varphi_i$, and the independence is the factorisation $\varphi(\prod a_k)=\prod\varphi(a_k)$. Independence and freeness are the two universal products compatible with the states; they agree on the first two mixed moments and differ from the fourth onward, the fourth mixed moment of two centred free variables being $\varphi(xyxy)=0$ against the independent $\varphi(x^2)\varphi(y^2)$.

*Proof.* The classical statement is the Fubini theorem for a product measure, with the state the expectation; the difference between the two products at the fourth moment is the comparison of the free recursion with the factorisation, and it is displayed for the centred case in the preceding theorem.

## The Free Central Limit Theorem

### The semicircle law

**Definition.** The **semicircle law** of variance $\sigma^2$ is the probability measure
$$
d\mu_\sigma(t)=\frac{1}{2\pi\sigma^2}\sqrt{4\sigma^2-t^2}\,\mathbf 1_{|t|\le2\sigma}\,dt .
$$

**Theorem (the free central limit theorem).** Let $x_1,x_2,\dots$ be free, identically distributed, self-adjoint with $\varphi(x_i)=0$ and $\varphi(x_i^2)=\sigma^2$. Then the distribution of
$$
\frac{x_1+\cdots+x_n}{\sqrt n}
$$
converges in moments to the semicircle law $\mu_\sigma$.

*Proof.* The moments of the sum are computed by the freeness recursion, in which the only surviving pairings of a word of length $2m$ are the non-crossing ones, and the count of the non-crossing pairings of $2m$ elements is the Catalan number $C_m$; hence $\varphi\bigl((\text{sum}/\sqrt n)^{2m}\bigr)\to\sigma^{2m}C_m$, and $C_m$ is the $2m$-th moment of $\mu_\sigma$. The odd moments vanish, and the convergence of the moments with the compactness of the supports gives the weak convergence.

### The moments and the Catalan numbers

**Theorem.** The moments of the standard semicircle law are
$$
\int t^{2m}\,d\mu_1(t)=C_m=\frac{1}{m+1}\binom{2m}{m},\qquad \int t^{2m+1}\,d\mu_1(t)=0 .
$$

*Proof.* The density integrates to the Catalan numbers, as the generating function $\sum_mC_mz^m=\frac{1-\sqrt{1-4z}}{2z}$ makes explicit; equivalently the moments satisfy $m_0=1$ and the recursion $m_{2m}=\sum_{k=0}^{m-1}m_{2k}m_{2m-2-2k}$, which is the recursion the non-crossing pairings obey.

## Free Cumulants and the $R$-Transform

### Definition

**Definition.** For a random variable $x$ the **free cumulants** $\kappa_n(x)$ are defined by the moment–cumulant recursion over the non-crossing partitions,
$$
\varphi(x^n)=\sum_{\pi\in NC(n)}\prod_{B\in\pi}\kappa_{|B|}(x),
$$
and the **$R$-transform** is $R_x(z)=\sum_{n\ge1}\kappa_n(x)z^{n-1}$.

**Theorem (additivity).** If $x$ and $y$ are free, then
$$
R_{x+y}=R_x+R_y ,
$$
that is, the free cumulants are additive under freeness, in the same way that the classical cumulants are additive under independence.

*Proof.* The moment–cumulant recursion over the non-crossing partitions factors across the free product, and the generating series of the non-crossing partitions of a sum splits into the two series; the additivity is the free analogue of the additivity of the logarithm of the characteristic function. The $R$-transform of the semicircle law of variance $\sigma^2$ is $R(z)=\sigma^2z$, from which the Catalan moments follow by the recursion.

## Worked Examples

**Example (the semicircle law).** For the semicircle of variance one the cumulants are $\kappa_1=0$, $\kappa_2=1$, $\kappa_n=0$ for $n\ge3$, the $R$-transform is $R(z)=z$, and the moments are the Catalan numbers $1,1,2,5,14,\dots$. The law is the free analogue of the Gaussian, whose $R$-transform is $R(z)=\sigma^2z$ as well, the differing cumulants beyond the second being zero in both cases.

**Example (the free Poisson law).** The free analogue of the Poisson law of parameter $\lambda$ has the $R$-transform $R(z)=\lambda/(1-z)$ and the density $\frac{1}{2\pi t}\sqrt{(b-t)(t-a)}$ on the interval $[a,b]=[(1-\sqrt\lambda)^2,(1+\sqrt\lambda)^2]$, with the free cumulants $\kappa_n=\lambda$ for every $n\ge1$; it is the limit law of the free analogue of the sum of the indicators, and it is the Marchenko–Pastur law of the random-matrix literature.

**Example (the circular element).** Let $s_1,s_2$ be free standard semicircular elements and put $c=(s_1+is_2)/\sqrt2$, the **circular element**. It is neither self-adjoint nor normal:
$$
cc^*-c^*c=\tfrac12\bigl[(s_1+is_2)(s_1-is_2)-(s_1-is_2)(s_1+is_2)\bigr]=i\,(s_2s_1-s_1s_2),
$$
which is nonzero because the free $s_1,s_2$ do not commute, and the involution pairs $c$ with $c^*$ in a way that is not a scalar commutator. The example shows that the involution is what supplies the positivity: the state is positive on $c^*c$ and on $cc^*$ alike, while the two products differ.

**Example (the classical independent case).** If the algebra is commutative and the state is the expectation, the moment–cumulant recursion over **all** partitions gives the classical cumulants and the analogue of the $R$-transform is the cumulant generating function, the logarithm of the Fourier transform; the free recursion is the same formula restricted to the non-crossing partitions, and the two agree through the second cumulant and differ from the third, exactly as the independence and the freeness differ from the fourth mixed moment.

## Failure of the Degenerate Cases

Non-commutative probability degenerates in four configurations. First, the state need not be faithful: when $\varphi(x^*x)=0$ for a nonzero $x$, the GNS form is only semi-definite, the representation has a kernel, and the element $x$ is invisible to the probability; the quotient by the kernel is required before the moments define a law. Second, a self-adjoint element need not have a determinate distribution: the moment sequence can fail Carleman's condition, and two measures with the same moments are then indistinguishable by the state, the free analogue of the moment problem of the commutative theory. Third, freeness requires the states on the subalgebras to be faithful for the reduced free product to be canonical; without faithfulness the free product depends on choices. Fourth, the free central limit theorem needs the finiteness of the second moment, and the convergence is in moments and hence only in the cases where the law is determined by them; without the second moment the free stable laws replace the semicircle, and the Catalan picture is lost.

## Summary

A non-commutative probability space is a unital involutive algebra $\mathcal{A}$ with a state $\varphi$, the elements are the random variables, the self-adjoint elements the real ones, and the GNS form $\langle x,y\rangle=\varphi(xy^*)$ is positive semi-definite and invariant so that the left multiplications satisfy $\pi(a)^*=\pi(a^*)$; the state is self-adjoint, real on the self-adjoint elements, and the moments of a self-adjoint element determine its distribution through the spectral theorem when they are determinate. Freeness is the independence of the free product: the moments of a mixed word with centred entries vanish when the adjacent entries lie in distinct subalgebras, the reduced free product is the universal pair with that property, and the classical independence is the tensor-product case. The free central limit theorem gives the semicircle law for the normalised sum of free identically distributed variables, with the Catalan numbers as its moments, and the free cumulants of the non-crossing partitions add under freeness, with the $R$-transform of the semicircle equal to $\sigma^2z$. The classical commutative case is *The Involution on the Algebra of Random Variables*, later in this category, the covariance form is *The Covariance Function and Hermitian Positivity*, and the states and the GNS construction are *Operator Algebras*, written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal{A},\varphi)$ | non-commutative probability space, algebra with a state |
| $x^*$, $x=x^*$ | the involution; the real (self-adjoint) random variables |
| $\langle x,y\rangle=\varphi(xy^*)$ | the GNS form |
| $\mathcal{H}=L^2(\mathcal{A},\varphi)$, $\pi$ | the GNS space and the left regular representation |
| $\mu_x$, $\varphi(x^n)=\int t^nd\mu_x$ | distribution of a self-adjoint $x$ |
| free | freeness of subalgebras or variables |
| $*_i(\mathcal{A}_i,\varphi_i)$ | the reduced free product |
| $\mu_\sigma$, $C_m$ | the semicircle law and the Catalan numbers |
| $\kappa_n$, $R_x(z)=\sum\kappa_nz^{n-1}$ | free cumulants and the $R$-transform |
| $R_{x+y}=R_x+R_y$ | additivity under freeness |

## Further Reading

- Dan-Virgil Voiculescu, "Symmetries of some reduced free product C*-algebras", in *Operator Algebras and their Connections with Topology and Ergodic Theory*, Lecture Notes in Mathematics 1132 (Springer, 1985), 556–588, for the free product and freeness.
- Dan-Virgil Voiculescu, Ken J. Dykema and Alexandru Nica, *Free Random Variables*, CRM Monograph Series 1 (American Mathematical Society, 1992), for the free central limit theorem and the $R$-transform.
- Alexandru Nica and Roland Speicher, *Lectures on the Combinatorics of Free Probability* (Cambridge University Press, 2006), for the non-crossing partitions and the free cumulants.
- Philippe Biane, "Free probability and the representation theory of the symmetric group", in *Free Probability Theory*, Fields Institute Communications 12 (American Mathematical Society, 1997), for the semicircle law and the Catalan combinatorics.
- Michel Ledoux and Dan-Virgil Voiculescu, *Free Probability and Operator Algebras* (European Mathematical Society, 2013), for the modern operator-algebraic treatment.
