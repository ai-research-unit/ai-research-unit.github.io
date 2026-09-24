
# __Ergodic Theory__

## Introduction

Ergodic theory is the study of a measure-preserving transformation of a probability space, and the question it asks is how the iterates of a point distribute themselves. The empirical evidence for the theory is the law of large numbers: for a sequence of independent and identically distributed random variables the sample means converge to the mean, and for a measure-preserving transformation the time averages converge to the space average, so that the independence is replaced by the invariance of the measure and the conclusion survives. Theorems of this kind — the pointwise ergodic theorem of Birkhoff and the mean ergodic theorem of von Neumann — are the fundamental results of the subject, and the quantitative refinement of the theory is entropy, which measures how fast a transformation generates information.

This article develops the general theory of a **single** measure-preserving transformation. It defines invariance and ergodicity, proves Poincaré's recurrence theorem, introduces the Koopman unitary operator as the spectral encoding of the dynamics, proves the mean and pointwise ergodic theorems with the Hopf maximal inequality, establishes the criteria for ergodicity and mixing, describes the ergodic decomposition of the invariant measures, develops Kolmogorov–Sinai entropy with the Shannon–McMillan–Breiman theorem and the Ornstein isomorphism theorem for Bernoulli shifts, and closes with Pesin's formula. The examples — rotations, the doubling map, the Gauss map of continued fractions, Bernoulli shifts, toral automorphisms — are developed as they arise.

Two boundaries are held exactly, and the first is stated again here because it is the sharpest in the part.

- The **ergodic theory of group actions** — the invariance, ergodicity and mixing of an action of a general locally compact group, the Følner averaging of an amenable group, the Mautner phenomenon, the Moore and Howe–Moore theorems, orbit equivalence and the ratio ergodic theorem, and the homogeneous examples — is *Ergodic Theory of Group Actions*. The two articles overlap in the von Neumann and Birkhoff theorems for the action of $\mathbb{Z}$, which are stated once there as standard mathematics and used, and are here **proved** in the sharp form they take for a single transformation; the present article is the measure-theoretic theory of one map, and the group-action article is the algebraic theory of a group acting. **The division of labour is asserted in the introduction of each article**.
- The **probability theory** used here — the measure-theoretic frame, independence, conditional expectation, the laws of large numbers and the central limit theorem, the martingale theory, the Markov chains and processes, and the Brownian motion — is the block of articles *Measure-Theoretic Probability* through *Brownian Motion and Stochastic Calculus*, and the probabilistic statements are cited from them. The **general measure theory** is *Measure Theory and Integration* and *Modes of Convergence*, and the **functional analysis** — the spectral theorem, the $L^2$ projection, the unitary operators, the Choquet theory of simplices — is *Banach and Hilbert Spaces* and *Operator Algebras*. The **dynamical applications** to homogeneous spaces are *Homogeneous Dynamics* and *Ratner's Theorems*; the **equidistribution** of orbits is *Equidistribution*; and the **random walks on groups**, where the ergodic theory of a convolution action is used, is. No physics is invoked.

Throughout, $(X,\mathcal{B},\mu)$ is a probability space, $T : X\to X$ is a measurable map, and $T$ is **measure-preserving** if $\mu(T^{-1}A) = \mu(A)$ for every $A \in \mathcal{B}$; the pair $(X,\mathcal{B},\mu,T)$ is then a **measure-preserving system**. Statements hold **a.e.** (almost everywhere) when they fail on a $\mu$-null set, and the probabilistic synonym *almost surely* is not used. The **invariant $\sigma$-algebra** is $\mathcal{I} = \{A \in \mathcal{B} : \mu(T^{-1}A\triangle A) = 0\}$, the **Koopman operator** is $U_Tf = f\circ T$, the **Kronecker** notation $e(\theta) = e^{2\pi i\theta}$ is used, and $\xi\vee\eta$ is the join of two partitions.

## Measure-Preserving Transformations

### Definitions and Examples

**Definition.** A measurable map $T : X\to X$ is **measure-preserving** if $\mu(T^{-1}A) = \mu(A)$ for all $A \in \mathcal{B}$, and **invertible** if it is a bimeasurable bijection with a measure-preserving inverse; a measure-preserving system is **ergodic** if $A \in \mathcal{I}$ implies $\mu(A) \in \{0,1\}$, and **nonsingular** if only $\mu(T^{-1}A) = 0 \iff \mu(A) = 0$.

**Example (circle rotations).** Let $X = \mathbb{R}/\mathbb{Z}$ with Lebesgue measure and $T(x) = x + \alpha \bmod 1$. The rotation preserves Lebesgue measure and is ergodic exactly when $\alpha$ is irrational; when $\alpha = p/q$ is rational the orbits are the cosets of the finite subgroup $\frac1q\mathbb{Z}/\mathbb{Z}$ and the invariant sets are the unions of them, so the system is not ergodic.

**Example (the doubling map).** On $[0,1)$ with Lebesgue measure, $T(x) = 2x \bmod 1$ preserves the measure and is ergodic; it is the one-sided Bernoulli shift on the binary digits, and the entropy is $\log 2$.

**Example (Bernoulli shifts).** Let $(p_1,\dots,p_k)$ be a probability vector and let $X = \{1,\dots,k\}^{\mathbb{Z}}$ with the product measure $\mu = \prod_{\mathbb{Z}}\sum_ip_i\delta_i$, the **Bernoulli shift** being the left translation $\sigma$ of the sequence. The system $(\sigma,\mu)$ is measure-preserving, invertible and ergodic; the entropy is $H(p) = \sum_ip_i\log(1/p_i)$, and the classification of these systems is Ornstein's theorem below.

**Example (the Gauss map).** Let $X = [0,1)$ and $T(x) = 1/x \bmod 1$ for $x \neq 0$, $T(0) = 0$. The Gauss measure $d\mu = \frac{1}{\log2}\frac{dx}{1+x}$ is preserved; the map is ergodic, and it generates the continued fraction expansion $x = [a_1,a_2,\dots]$ with $a_n = \lfloor T^{n-1}x\rfloor$ for $n \geq 1$. The entropy is $\pi^2/(6\log2)$, and the ergodic theorem applied to the digit functions gives the almost-sure statements of the metric theory of continued fractions: the limiting frequency of the digit $k$ is $\frac{1}{\log2}\log\frac{(k+1)^2}{k(k+2)}$, and the limiting behaviour of the convergents is governed by the Lyapunov exponent of $T$.

**Example (toral automorphisms).** Let $X = \mathbb{R}^2/\mathbb{Z}^2$ with Lebesgue measure and let $A \in SL_2(\mathbb{Z})$; the induced map $T_A$ preserves the measure. When $|\operatorname{tr}A| > 2$ the eigenvalues are real and one is larger than $1$ in modulus; the map is ergodic, mixing and of positive entropy $\log|\lambda|$, with $\lambda$ the larger eigenvalue. The automorphism is the prototype of the hyperbolic behaviour exploited in *Homogeneous Dynamics*.

### Poincaré Recurrence

**Theorem (Poincaré recurrence).** Let $T$ be measure-preserving and let $A \in \mathcal{B}$ with $\mu(A) > 0$. Then for a.e. $x \in A$ there are infinitely many $n \geq 1$ with $T^nx \in A$.

*Proof.* Let $N = \{x \in A : T^nx \notin A \text{ for all } n \geq 1\}$ be the set of points that never return. The sets $N, T^{-1}N, T^{-2}N, \dots$ are pairwise disjoint: if $T^{-i}N\cap T^{-j}N\neq\varnothing$ with $i<j$, then a point of $N$ is sent by $T^{j-i}$ into $N\subseteq A$, contradicting the definition of $N$. Since $T$ preserves the measure, all the sets $T^{-k}N$ have the same measure, and pairwise disjointness forces $\mu(N) = 0$. Hence a.e. point of $A$ returns at least once; applying the same argument to the measure-preserving system restricted to the return times gives infinitely many returns. $\square$

The recurrence theorem is the first indication that measure-preserving dynamics is recurrent: a positive-measure set is visited infinitely often by almost every orbit that meets it. It is also the reason the asymptotic statements below are meaningful, and its quantitative form is Kac's theorem at the end of the next section.

### The Koopman Operator

**Definition.** The **Koopman operator** of a measure-preserving $T$ is the linear isometry

$$
U_T : L^2(X,\mu)\to L^2(X,\mu), \qquad U_Tf = f\circ T.
$$

If $T$ is invertible then $U_T$ is unitary, and $U_T$ is the representation of $\mathbb{Z}$ on $L^2$ induced by the action; its properties encode the dynamics.

**Proposition.** If $T$ is invertible then $U_T$ is unitary and $U_T^{-1} = U_{T^{-1}}$; the constant functions span the **fixed space** $\ker(U_T - I)$, and the orthogonal complement of the fixed space is the closed span of the **coboundaries** $\{f\circ T - f : f \in L^2\}$.

*Proof.* The unitarity follows from the change of variables, since $T$ preserves $\mu$: $\langle U_Tf, U_Tg\rangle = \int f(Tx)\overline{g(Tx)}\,d\mu(x) = \int f\bar g\,d\mu$ by the measure-preserving property. The identification of the coboundaries is the standard orthogonal decomposition $L^2 = \ker(U-I)\oplus\overline{\operatorname{Im}(U-I)}$ for a unitary operator, valid because the two spaces are orthogonal — $\langle f\circ T - f, h\rangle = 0$ for $h$ fixed — and because the orthogonal complement of the image is the kernel for a normal operator. $\square$

The coboundary decomposition is the operator-theoretic form of the ergodic theorems: the orthogonal projection onto the fixed space is the limit of the averages of the powers of $U_T$, and the coboundary part averages to zero. The same decomposition in the unitary representation of a group is the subject of *Ergodic Theory of Group Actions* and of the spectral theory of *Noncommutative Harmonic Analysis*.

## Ergodicity and Its Criteria

### Equivalent Forms

**Theorem (ergodicity criteria).** For an invertible measure-preserving $T$ the following are equivalent:

1. $T$ is ergodic;
2. every $f \in L^2$ with $f\circ T = f$ a.e. is constant a.e.;
3. the fixed space of $U_T$ on $L^2$ is one-dimensional;
4. for every $A, B \in \mathcal{B}$ of positive measure there is $n \in \mathbb{Z}$ with $\mu(T^nA \cap B) > 0$;
5. for all $A,B \in \mathcal{B}$, $\frac{1}{n}\sum_{k=0}^{n-1}\mu(T^{-k}A\cap B) \to \mu(A)\mu(B)$.

*Proof.* The equivalence of 1, 2 and 3 is immediate from the definitions: an invariant function is a limit of invariant simple functions, and the invariant sets generate the invariant functions. The equivalence with 4 is the argument used for the group-action dichotomy: if $\mu(T^nA\cap B) = 0$ for all $n$ and $A$ is invariant with $0 < \mu(A) < 1$, take $B = X\setminus A$. The equivalence with 5 is the mean ergodic theorem applied to the indicator functions, since the average of the correlations is the inner product of the averages. $\square$

The criterion 5 is the form in which ergodicity is checked in practice, and it is the first appearance of the mixing hierarchy: ergodicity is the convergence of the **Cesàro** averages of the correlations, and the stronger property asks for the convergence of the correlations themselves.

### The Koopman Spectrum and the Classification

**Definition.** The system is **mixing** (or strongly mixing) if for all $A,B \in \mathcal{B}$,

$$
\mu(T^{-n}A\cap B) \longrightarrow \mu(A)\mu(B) \quad \text{as } n\to\infty;
$$

it is **weakly mixing** if the Cesàro averages of the correlations converge as in criterion 5 of the previous theorem with the absolute values, that is $\frac1n\sum_{k<n}|\mu(T^{-k}A\cap B) - \mu(A)\mu(B)|\to0$; and it is **rigid** if there is a sequence $n_k\to\infty$ with $\mu(T^{-n_k}A\triangle A)\to0$ for every $A$.

**Theorem (spectral classification).** For an invertible measure-preserving $T$:

1. $T$ is ergodic if and only if $1$ is a simple eigenvalue of $U_T$;
2. $T$ is weakly mixing if and only if $1$ is the only eigenvalue of $U_T$, that is, the system has discrete spectrum $1$ alone;
3. $T$ is mixing if and only if $\langle U_T^nf,g\rangle \to \langle Pf, \mathbf{1}\rangle\langle \mathbf{1},g\rangle$ for all $f,g \in L^2$, where $P$ is the projection onto the constants.

*Proof (sketch).* The first statement is a restatement of criterion 3 above. For the second, the correlation $n\mapsto\langle U_T^nf,g\rangle$ is a positive-definite sequence; a positive-definite sequence whose Cesàro absolute means vanish must have vanishing Fourier coefficients at nonzero frequencies, so no eigenvalue other than $1$ can occur, and conversely a nonconstant eigenfunction produces a correlation whose average does not vanish. The third statement is the definition rewritten with $f = \mathbf{1}_A$, $g = \mathbf{1}_B$ and the density of the indicators in $L^2$; the limit is the announced one. $\square$

The classification shows that the ergodic hierarchy is a hierarchy of the spectrum of the Koopman operator: ergodicity says the fixed space is one-dimensional, weak mixing that the point spectrum is trivial on the orthogonal complement of the constants, and mixing that the correlations decay in the mean. Weak mixing is also characterised by the ergodicity of the product system $T\times T$, and mixing implies weak mixing which implies ergodicity, with the circle rotation showing that ergodicity does not imply weak mixing, and the weakly mixing but non-mixing systems of rank-one constructions showing that weak mixing does not imply mixing.

**Example.** An irrational rotation is ergodic and not weakly mixing: its Koopman operator has the full circle group of eigenvalues, since $U_T e(nx) = e(n\alpha)e(nx)$. A Bernoulli shift is mixing: $\mu(\sigma^{-n}A\cap B)\to\mu(A)\mu(B)$ because the events depend on coordinates far apart, and the correlations decay. A rigid system is not mixing, and the contrast between the rigidity of a rotation and the mixing of a Bernoulli shift is the motivating dichotomy of the subject.

## The Ergodic Theorems

### The Mean Ergodic Theorem

**Theorem (von Neumann).** Let $T$ be measure-preserving and let $P$ be the orthogonal projection of $L^2(X,\mu)$ onto the fixed space $\ker(U_T - I)$. Then for every $f \in L^2$,

$$
\frac{1}{n}\sum_{k=0}^{n-1}U_T^kf \longrightarrow Pf \qquad \text{in } L^2.
$$

*Proof.* Decompose $f = Pf + (f - Pf)$ according to $L^2 = \ker(U-I)\oplus\overline{\operatorname{Im}(U-I)}$. The first summand is fixed and its averages are $Pf$. For the second, it suffices to treat $f = g\circ T - g$: the averages telescope,

$$
\frac{1}{n}\sum_{k=0}^{n-1}U^k(g\circ T - g) = \frac{1}{n}\bigl(U^ng - g\bigr),
$$

whose norm is at most $2\|g\|_2/n\to0$; the general element of the closure of the image is handled by approximation. $\square$

The theorem is the ergodic theorem in the mean, and it is a statement about the operator $U$ alone: it holds for every contraction of a Hilbert space (the **von Neumann ergodic theorem** for isometries), with the projection onto the fixed space as the limit. If $T$ is ergodic then $Pf = \int f\,d\mu$ is the constant function of the mean, and the theorem is the convergence of the averages to the space average. The theorem does not require the pointwise convergence, which is the content of the next result.

### The Pointwise Ergodic Theorem

**Definition.** For $f \in L^1(X,\mu)$ the **Birkhoff sums** are $S_nf = \sum_{k=0}^{n-1}f\circ T^k$ and the **maximal function** is $(Mf)(x) = \sup_{n\geq1}\frac{1}{n}S_nf(x)$.

**Theorem (Hopf maximal inequality).** Let $f\in L^1$ be real-valued and let $M_Nf = \max_{0\leq k\leq N}S_kf$. Then

$$
\int_{\{M_Nf > 0\}} f\,d\mu \geq 0 \qquad \text{for every } N.
$$

*Proof.* Decompose the set where the maximum is positive according to the first time $k \leq N$ at which $S_kf > 0$, and use the translation invariance of the measure: on the piece where the first positive partial sum occurs at $k$, the sum $S_kf$ is at least the later increments, so
$\int_{\{M_Nf>0\}}f\,d\mu = \sum_{k=0}^{N}\int_{\{\text{first positive at }k\}}f\,d\mu \geq 0$. $\square$

**Theorem (Birkhoff pointwise ergodic theorem).** Let $T$ be measure-preserving and let $f \in L^1(X,\mu)$. Then the averages converge a.e. and in $L^1$:

$$
\frac{1}{n}\sum_{k=0}^{n-1}f(T^kx) \longrightarrow f^*(x) \qquad \text{a.e., with } f^* \in L^1, \quad f^*\circ T = f^* \text{ a.e.,} \quad \int f^*\,d\mu = \int f\,d\mu.
$$

If $T$ is ergodic then $f^* = \int f\,d\mu$ a.e.

*Proof (sketch).* The Hopf maximal inequality applied to $\pm(f - g)$ for a bounded invariant $g$ controls the set where the averages differ from a constant by more than $\varepsilon$; the maximal inequality of Hopf and the density of the bounded functions in $L^1$ show that the set of points where $\limsup$ and $\liminf$ of the averages differ has measure zero. The limit $f^*$ is invariant because the averages are and the limit is measurable with respect to the invariant $\sigma$-algebra; the identity $\int f^* = \int f$ follows from the mean ergodic theorem, which identifies the $L^1$ limit of the averages with the conditional expectation $\mathbb{E}[f\mid\mathcal{I}]$. $\square$

The theorem is the pointwise form of the law of large numbers: for the Bernoulli shift the invariant $\sigma$-algebra is trivial, and the conclusion is the classical strong law of *Laws of Large Numbers and the Central Limit Theorem*. In general the limit is the conditional expectation onto the invariant sets, $\mathbb{E}[f\mid\mathcal{I}]$, and this is the sharp statement: the time average converges to the space average along the ergodic components, and the decomposition into ergodic components is the subject of the section after the next.

### Kac's Recurrence Theorem

**Theorem (Kac).** Let $T$ be ergodic and measure-preserving on a probability space, let $A \in \mathcal{B}$ with $\mu(A) > 0$, and let $\tau_A(x) = \inf\{n \geq 1 : T^nx \in A\}$ be the first return time. Then $\int_A\tau_A\,d\mu = 1$.

*Proof.* Apply the ergodic theorem to the ergodic system induced on $A$ by the first-return map, or equivalently apply the ergodic theorem to $\mathbf{1}_A$ and count the visits: the proportion of time spent in $A$ is $\mu(A)$, and the average return time is the reciprocal of the frequency of visits, which gives the identity after the normalisation by $\mu(A)$. The precise derivation uses the Kac formula $\int_A\tau_A\,d\mu = 1$ for a probability measure, which is the ergodic theorem for the induced transformation. $\square$

Kac's theorem quantifies Poincaré recurrence: the mean return time to $A$ is $1/\mu(A)$, so a small set is revisited only after a long time. It is the prototype of the return-time statements used in the theory of the continued fraction map and in the recurrence of the homogeneous flows of *Ergodic Theory of Group Actions*.

## Entropy

### Kolmogorov–Sinai Entropy

**Definition.** Let $\xi = \{A_1,\dots,A_k\}$ be a finite partition of $X$. Its **entropy** is $H(\xi) = -\sum_i\mu(A_i)\log\mu(A_i)$, and the entropy of $T$ with respect to $\xi$ is

$$
h_\mu(T,\xi) = \lim_{n\to\infty}\frac{1}{n}H\!\left(\bigvee_{k=0}^{n-1}T^{-k}\xi\right),
$$

the limit existing because the sequence is subadditive. The **Kolmogorov–Sinai entropy** is $h_\mu(T) = \sup_\xi h_\mu(T,\xi)$, the supremum over finite partitions.

**Theorem (Kolmogorov–Sinai).** If $\xi$ is a **generator** — that is, the partitions $T^{-k}\xi$, $k \geq 0$, generate the $\sigma$-algebra $\mathcal{B}$ up to null sets — then $h_\mu(T) = h_\mu(T,\xi)$.

The entropy is an isomorphism invariant: conjugate systems have the same entropy, so the entropy separates systems that are not isomorphic, and it is the principal computable invariant of ergodic theory. The Kolmogorov–Sinai theorem reduces its computation to a single partition for the standard examples: the binary partition generates the doubling map and gives $\log 2$; the digit partition generates the Bernoulli shift and gives $H(p)$; the continued fraction partition together with the Gauss measure gives $\pi^2/(6\log2)$; and a toral automorphism has entropy $\log|\lambda|$ by the Adler–Weiss computation.

### The Shannon–McMillan–Breiman Theorem

**Theorem (Shannon–McMillan–Breiman).** Let $T$ be ergodic and measure-preserving and let $\xi$ be a finite partition. Then

$$
-\frac{1}{n}\log\mu\bigl(\xi^{(n)}(x)\bigr) \longrightarrow h_\mu(T,\xi) \qquad \text{a.e. and in } L^1,
$$

where $\xi^{(n)} = \bigvee_{k=0}^{n-1}T^{-k}\xi$ and $\xi^{(n)}(x)$ is the atom of $\xi^{(n)}$ containing $x$.

The theorem is the ergodic theorem for the information function, and it is the reason the entropy is the exponential rate of decay of the measure of the atom: the typical atom of the $n$-fold refinement has measure $e^{-nh_\mu(T,\xi)}$. Its proof applies the martingale convergence theorem of *Martingales* to the conditional information functions — which form a reverse martingale as the conditioning $\sigma$-algebra shrinks — together with the ergodic theorem for the limiting term, and it is the bridge between entropy and the pointwise ergodic theory.

### Bernoulli Shifts and Ornstein's Theorem

**Theorem (Ornstein isomorphism theorem).** Two invertible Bernoulli shifts with probability vectors $p$ and $q$ are isomorphic — there is a measure-preserving invertible map intertwining the two shifts — if and only if $H(p) = H(q)$. More generally, the entropy is a complete invariant for the invertible Bernoulli shifts.

The theorem is the classification of the Bernoulli shifts, and it is the deepest result of the classical theory: entropy, which is only an invariant, is also sufficient to distinguish the Bernoulli systems. The proof uses the **very weak Bernoulli** property and the machinery of joinings; the same methods classify the Kolmogorov automorphisms and the Bernoulli flows. The result is the reason the entropy is the central numeric invariant of ergodic theory, and it is the model for the classification results of smooth ergodic theory.

### Pesin's Formula

**Theorem (Ruelle's inequality and Pesin's formula).** Let $T$ be a $C^{1+\alpha}$ diffeomorphism of a compact smooth manifold preserving an ergodic measure $\mu$. Then Ruelle's inequality holds:

$$
h_\mu(T) \leq \int \sum_{\lambda_i(x) > 0}\lambda_i(x)\,d\mu(x),
$$

where the $\lambda_i(x)$ are the Lyapunov exponents of $T$ at $x$ and the sum is over the positive ones; and if in addition $\mu$ has no zero Lyapunov exponents, then the **Pesin entropy formula**

$$
h_\mu(T) = \int \sum_{\lambda_i(x) > 0}\lambda_i(x)\,d\mu(x)
$$

holds.

Pesin's formula is the smooth ergodic theorem: the entropy, which is a measure-theoretic invariant, equals the total exponential expansion of the tangent map. It is the reason the entropy of a toral automorphism is $\log|\lambda|$ — the single Lyapunov exponent of the hyperbolic matrix — and it is the point of contact of ergodic theory with the hyperbolic dynamics of *Homogeneous Dynamics* and the geodesic flows of *Ergodic Theory of Group Actions*. The theorem is stated here as standard mathematics for the use of the entropy theory, with the citation to Pesin in the Further Reading; the general theory of Lyapunov exponents, the Oseledets theorem and the smooth ergodic theory built on it are the subject of the dynamical-systems block of the menu written in parallel, and are not developed here.

## The Ergodic Decomposition

**Theorem (ergodic decomposition).** Let $T$ be a measure-preserving transformation on a standard Borel probability space. Then

$$
\mu = \int \mu_x\, d\mu(x),
$$

where $\mu_x$ is the conditional measure on the atom of the invariant $\sigma$-algebra containing $x$; each $\mu_x$ is $T$-invariant and ergodic, and $\mu_x = \mu_y$ for $\mu$-a.e. $y$ in the atom. The set of $T$-invariant probability measures is a Choquet simplex whose extreme points are exactly the ergodic measures.

The theorem is the decomposition of an arbitrary invariant measure into ergodic components, and it is the reason the ergodic theorems can be stated for arbitrary systems: the time average of $f$ is the function $x\mapsto\int f\,d\mu_x$, which is constant on the atoms of the invariant $\sigma$-algebra and hence is the conditional expectation $\mathbb{E}[f\mid\mathcal{I}]$. The decomposition is the abstract version of the decomposition of a measure into its ergodic pieces in the classical examples — the countable family for a rational rotation, the continuum for the rotations of a circle, the family over the base of a skew product — and its proof uses the Choquet theorem for compact convex sets of measures and the Rohlin theory of the conditional measures.

## Summary

A measure-preserving system is a probability space with a transformation that preserves the measure; its invariant sets form the invariant $\sigma$-algebra, and the system is ergodic when that algebra is trivial. Poincaré's recurrence theorem states that a positive-measure set is revisited infinitely often by almost every orbit that meets it, and Kac's theorem computes the mean return time as the reciprocal of the measure. The Koopman operator $U_Tf = f\circ T$ is a unitary operator on $L^2$, encoding the dynamics: ergodicity is the simplicity of its eigenvalue $1$, weak mixing the absence of other eigenvalues, and mixing the decay of the correlations, so that the ergodic hierarchy is a hierarchy of the spectrum.

The von Neumann mean ergodic theorem states that the Cesàro averages of the powers of the Koopman operator converge in $L^2$ to the orthogonal projection onto the fixed space, with a proof that reduces to the telescoping of the coboundaries. The Birkhoff pointwise ergodic theorem states that the time averages of an integrable function converge almost everywhere and in $L^1$ to an invariant limit with the same integral, the limit being the conditional expectation onto the invariant $\sigma$-algebra; the Hopf maximal inequality is the maximal estimate behind the proof, and the theorem contains the strong law of large numbers as the case of the Bernoulli shift. The ergodic decomposition writes an invariant measure as an integral of ergodic ones, with the ergodic measures as the extreme points of the simplex of invariant probabilities.

The quantitiative refinement of the theory is entropy. The Kolmogorov–Sinai entropy is the supremum over finite partitions of the asymptotic entropy of the refinements, equal to the entropy of any generator by the Kolmogorov–Sinai theorem; the Shannon–McMillan–Breiman theorem states that the information of the typical atom decays at the exponential rate of the entropy; and Ornstein's theorem classifies the Bernoulli shifts by their entropy. Pesin's formula identifies the entropy of a smooth system with the total positive Lyapunov exponent, connecting the measure-theoretic invariant with the expansion of the derivative. The circle rotations, the doubling map, the Gauss map, the Bernoulli shifts and the toral automorphisms are the standard examples, and the group-action generalisation of the whole subject is *Ergodic Theory of Group Actions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\mathcal{B},\mu,T)$ | Measure-preserving system |
| a.e. | Almost everywhere; the probabilistic synonym a.s. is not used in this article |
| $\mathcal{I}$ | Invariant $\sigma$-algebra |
| ergodic | every invariant set has measure $0$ or $1$ |
| $U_Tf = f\circ T$ | Koopman operator; unitary when $T$ is invertible |
| $U_T^k$, coboundary | iterates; $g\circ T - g$ |
| mixing, weakly mixing, rigid | $\mu(T^{-n}A\cap B)\to\mu(A)\mu(B)$; Cesàro version; $\mu(T^{-n_k}A\triangle A)\to0$ |
| $S_nf$, $Mf$, $M_Nf$ | Birkhoff sums, maximal function, truncated maximum |
| von Neumann, Birkhoff | mean and pointwise ergodic theorems |
| $f^* = \mathbb{E}[f\mid\mathcal{I}]$ | Invariant limit of the time averages |
| $\tau_A$, Kac | first return time; $\int_A\tau_A\,d\mu=1$ |
| $H(\xi)$, $h_\mu(T,\xi)$, $h_\mu(T)$ | partition entropy, entropy with respect to $\xi$, Kolmogorov–Sinai entropy |
| generator | partition whose translates generate $\mathcal{B}$ |
| Shannon–McMillan–Breiman | $-\frac1n\log\mu(\xi^{(n)}(x))\to h_\mu(T,\xi)$ |
| Bernoulli shift, $H(p)$ | shift on $\{1,\dots,k\}^{\mathbb{Z}}$, its entropy |
| Pesin | $h_\mu(T)=\int\sum_{\lambda_i>0}\lambda_i\,d\mu$ |
| ergodic decomposition | $\mu=\int\mu_x\,d\mu(x)$, $\mu_x$ ergodic |



## Further Reading

- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the ergodic theorems, mixing, the ergodic decomposition and entropy.
- Karl Petersen, *Ergodic Theory* (Cambridge University Press, 1983), for a systematic account including the spectral theory and the classification results.
- I. P. Cornfeld, S. V. Fomin and Ya. G. Sinai, *Ergodic Theory* (Springer, 1982), for the entropy theory, the Shannon–McMillan–Breiman theorem and the Ornstein isomorphism theorem.
- Donald S. Ornstein, *Ergodic Theory, Randomness, and Dynamical Systems* (Yale University Press, 1974), for the very weak Bernoulli property and the classification of Bernoulli shifts.
- George D. Birkhoff, "Proof of the ergodic theorem", *Proceedings of the National Academy of Sciences* 17 (1931), 656–660, and John von Neumann, "Proof of the quasi-ergodic hypothesis", *Proceedings of the National Academy of Sciences* 18 (1932), 70–82, for the two ergodic theorems.
- Eberhard Hopf, *Ergodentheorie* (Springer, 1937), for the maximal inequality and the ratio ergodic theorem.
- Mark Kac, "On the notion of recurrence in discrete stochastic processes", *Bulletin of the American Mathematical Society* 53 (1947), 1002–1010, for the return-time theorem.
- A. N. Kolmogorov, "A new metric invariant of transitive dynamical systems and automorphisms of Lebesgue spaces", *Doklady Akademii Nauk SSSR* 119 (1958), 861–864, and Ya. G. Sinai, "On the notion of entropy of a dynamical system", *Doklady Akademii Nauk SSSR* 124 (1959), 768–771, for the entropy of a dynamical system.
- Ya. B. Pesin, "Characteristic Lyapunov exponents and smooth ergodic theory", *Russian Mathematical Surveys* 32 (1977), 55–114, for the entropy formula.
- Manfred Einsiedler and Thomas Ward, *Ergodic Theory with a View towards Number Theory* (Springer, 2011), for the ergodic theory of homogeneous flows and its arithmetic applications.
