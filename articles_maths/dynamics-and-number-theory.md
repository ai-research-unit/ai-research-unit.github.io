
# __Dynamics and Number Theory__

## Introduction

The dynamical systems of arithmetic origin are those whose orbits encode the arithmetic of a number: the **Gauss map** $x\mapsto\{1/x\}$ produces the continued fraction expansion of $x$ and is ergodic with respect to the Gauss measure $\frac{dx}{(1+x)\log2}$, so that the arithmetic statistics of almost every real number become an instance of the Birkhoff ergodic theorem; the **$\beta$-transformation** $x\mapsto\beta x\bmod1$ produces the expansions in a non-integer base and has entropy $\log\beta$; the rotations of the circle produce the Sturmian codings and the three-distance structure; and the whole continued fraction theory reappears as the symbolic dynamics of the **geodesic flow on the modular surface**, whose return map to a cross-section is the Gauss map. The subject is therefore the meeting point of three theories: the ergodic theory of *Ergodic Theory*, the symbolic dynamics of *Symbolic Dynamics*, and the homogeneous dynamics of *Homogeneous Dynamics*, *Ratner's Theorems* and *Equidistribution*. What is specific to the subject is that the invariant measure, the entropy and the recurrence rates carry arithmetic information — the mean rate of growth of the continued fraction denominators is $\frac{\pi^2}{12\log2}$, the entropy of the Gauss map is $\frac{\pi^2}{6\log2}$, the almost-sure geometric mean of the partial quotients is the Khinchin constant — so that the dynamics computes arithmetic constants.

The article begins with the Gauss map: the continued fraction algorithm, the expansion $x=[0;a_1,a_2,\dots]$, the Gauss measure and its invariance, the **Gauss–Kuzmin theorem** on the distribution of the iterates and its rate, and the **Gauss–Kuzmin–Wirsing operator** with its spectral gap. The statistics follow: the law of the partial quotients, the infinite mean, the law of large numbers and the constant of Lévy, the theorem of Khinchin on the geometric mean, the central limit theorem for the digits, and the relation of the expansion to the Diophantine approximation, with the Khinchin and Jarník theorems and the dimension of the badly approximable numbers. The article then turns to the **homogeneous dynamics** of the modular group: the modular surface, the geodesic flow, the cross-section whose return map is the Gauss map, the ergodicity and mixing of the flow, and the equidistribution results that put the continued fraction statistics into the framework of *Homogeneous Dynamics* and *Ratner's Theorems*. It closes with the further arithmetic systems: the $\beta$-shifts, the rotations and the three-distance theorem, the theorem of Furstenberg on the $\times2$ and $\times3$ orbits, and the open problems of the arithmetic dynamics, the Collatz map among them.

The measure-preserving transformations, the ergodicity, the mixing, the entropy and the Birkhoff and von Neumann theorems are those of *Ergodic Theory*; the shift spaces, the $\beta$-shifts and the subshifts are those of *Symbolic Dynamics*; the topological dynamics and the topological entropy are those of *Topological Dynamics*; the rotations, the equidistribution and the Weyl criterion are those of *Equidistribution*; the modular surface, the unipotent flows and the classification theorems are those of *Homogeneous Dynamics*, *Ratner's Theorems* and *Lattices in Lie Groups*; the hyperbolic geometry of the modular surface is that of *Hyperbolic Geometry*; the geodesic flow and its ergodicity are standard. The arithmetic of the continued fractions of the rational numbers, as a chapter of the synthetic study of that number system, belongs to Part V .

No physics is invoked.

## The Gauss Map and Continued Fractions

### The Expansion

**Definition.** The **Gauss map** is $T:(0,1]\to[0,1)$, $T(x)=\frac1x-\bigl\lfloor\frac1x\bigr\rfloor=\{\frac1x\}$, with $T(0)=0$ by convention; the **partial quotients** of $x \in(0,1)$ are $a_n(x)=\bigl\lfloor\frac{1}{T^{n-1}x}\bigr\rfloor \in\mathbb{N}$, and the corresponding **continued fraction expansion** is

$$
x=\cfrac{1}{a_1+\cfrac{1}{a_2+\cfrac{1}{a_3+\cdots}}}=[0;a_1,a_2,a_3,\dots].
$$

The expansion terminates exactly for the rationals, so that the Gauss map is the dynamics of the continued fraction algorithm: the **convergents** $\frac{p_n}{q_n}=[0;a_1,\dots,a_n]$ satisfy the recursions $p_n=a_np_{n-1}+p_{n-2}$, $q_n=a_nq_{n-1}+q_{n-2}$ with $\frac{p_0}{q_0}=\frac01$, $\frac{p_1}{q_1}=\frac{1}{a_1}$, and the error is

$$
\Bigl|x-\frac{p_n}{q_n}\Bigr|=\frac1{q_n\bigl(q_n+T^nx\,q_{n-1}\bigr)},
\qquad
\frac{q_n}{q_{n-1}}=a_n+\frac{q_{n-2}}{q_{n-1}} .
$$

**Theorem (the Gauss measure).** The measure

$$
\mu(A)=\frac1{\log2}\int_A\frac{dx}{1+x} \qquad (A \subseteq(0,1] \text{ measurable})
$$

is $T$-invariant and ergodic; it is the unique absolutely continuous invariant probability measure of the Gauss map. Its density $\frac{1}{(1+x)\log2}$ is the **Gauss density**, and the invariance is the identity

$$
\frac1{\log2}\int_0^1\frac{f(Tx)}{1+x}\,dx=\frac1{\log2}\int_0^1\frac{f(x)}{1+x}\,dx ,
$$

which for the branches $T|_{(\frac{1}{k+1},\frac1k]}(x)=\frac1x-k$ reduces to a telescoping sum.

*Proof.* The preimage of $(y,1]$ under $T$ is the union of the intervals $(\frac{1}{k+y},\frac1k)$, $k \ge1$; summing the Gauss measure of these intervals gives the identity by the telescoping of $\log(1+\frac{1}{k})-\log(1+\frac{1}{k+y})$, and the identity is the stated invariance. The ergodicity follows from the exactness of $T$, or from the spectral gap of the Gauss–Kuzmin–Wirsing operator acting on the functions of bounded variation, which makes the invariant density unique; the uniqueness of the absolutely continuous invariant measure is then the standard consequence. $\square$

**Theorem (Gauss–Kuzmin).** For every interval $A \subseteq(0,1]$,

$$
\mu(T^{-n}A)\to\mu(A) \qquad (n\to\infty),
$$

so that the distribution of the preimages converges to the Gauss measure, whatever the initial measure; more precisely, the **Gauss–Kuzmin–Wirsing** theorem gives the rate

$$
\mu(T^{-n}A)=\mu(A)+O(\lambda^n)
$$

with $\lambda<1$ an explicit spectral radius, and the convergence is exponentially fast for the classes of sets and functions on which the transfer operator has a spectral gap. For Lebesgue-almost every $x$, the sequence $T^nx$ is equidistributed with respect to $\mu$.

### The Gauss–Kuzmin–Wirsing Operator

**Definition.** The **Gauss–Kuzmin–Wirsing operator** (the transfer operator of the Gauss map) is

$$
(\mathcal Pf)(x)=\sum_{k\ge1}\frac{1}{(x+k)^2}f\Bigl(\frac1{x+k}\Bigr),
$$

acting on the functions on $[0,1]$; the Gauss density $h(x)=\frac{1}{(1+x)\log2}$ satisfies $\mathcal Ph=h$, and more generally $\mathcal P$ is the adjoint of the Koopman operator $f\mapsto f\circ T$ with respect to the Lebesgue measure, so that $\mu$ is invariant exactly when $h$ is a fixed point.

**Theorem (spectral gap; Wirsing, Babenko, Mayer).** The operator $\mathcal P$ acting on a suitable Banach space of holomorphic functions on the disc $|z-1|<r$ with $r>\frac12$, or on the functions of bounded variation on $[0,1]$, has the eigenvalue $1$ with a simple eigenfunction the Gauss density, its remaining spectrum inside a disc of radius strictly less than $1$, and in particular an isolated second eigenvalue $\lambda_2=-0.303663\ldots$, the **Gauss–Kuzmin–Wirsing constant**; consequently the convergence in the Gauss–Kuzmin theorem is exponentially fast with rate $|\lambda_2|$ up to the logarithmic factor of the variation norm.

*Proof (sketch).* One shows that $\mathcal P$ is a compact perturbation of a rank-one operator on the appropriate analytic space, using the analyticity of the branches and the decay of the coefficients, and that the eigenvalue $1$ is simple because the fixed point equation $\mathcal Pf=f$ has the unique analytic solution $h$ up to scalars; the compactness gives the discrete spectrum off the unit circle and the numerical value of $\lambda_2$ is computed from the integral equation of the operator. $\square$

### The Natural Extension and Exactness

**Definition.** The **natural extension** of the Gauss map is the invertible map $\mathcal T$ of the square $[0,1]^2$ given by

$$
\mathcal T(x,y)=\Bigl(Tx,\ \frac{1}{a(x)+y}\Bigr), \qquad a(x)=\Bigl\lfloor\frac1x\Bigr\rfloor ,
$$

with $\mathcal T(0,y)=(0,y)$ and $\mathcal T(x,0)$ defined by continuity; it preserves the probability measure

$$
d\bar\mu=\frac{1}{\log2}\,\frac{dx\,dy}{(1+xy)^2},
$$

projects onto the Gauss map in the first coordinate and onto the backward continued fraction map in the second, and is the two-dimensional system whose return map is the cross-section of the modular flow of the next section.

**Remark (normalisation and invariance).** The density $\frac{1}{\log2}(1+xy)^{-2}$ is a probability density on the square: the inner integral is $\int_0^1\frac{dx}{(1+xy)^2}=\frac{1}{1+y}$, and $\frac1{\log2}\int_0^1\frac{dy}{1+y}=1$. The invariance of $\bar\mu$ under $\mathcal T$ is the two-dimensional form of the telescoping identity that gives the invariance of the Gauss measure, and it is proved by the same change of variables in each of the branches.

**Theorem (exactness and decorrelation).** The Gauss map is exact: the tail $\sigma$-algebra $\bigcap_{n\ge0}T^{-n}\mathcal B$ is trivial, and consequently it is ergodic and mixing for the Gauss measure. The decay of correlations of Hölder functions is exponential, with the rate given by the spectral radius of the Gauss–Kuzmin–Wirsing operator on the complement of the eigenvalue $1$; the natural extension inherits the exponential mixing, and it is Bernoulli, so the continued fraction process is Bernoulli up to the natural extension. The mixing is the dynamical statement behind the convergence of the distributions in the Gauss–Kuzmin theorem and behind the limit theorems of the next section.

*Proof (sketch).* The exactness is proved by showing that the transfer operator sends the functions of bounded variation into a space on which it is a strict contraction of the part with mean zero; the Bernoulli property follows from the very weak Bernoulli condition verified by the bounded distortion of the branches of $T^n$. $\square$

## Statistics, Equidistribution and Diophantine Approximation

### The Law of the Partial Quotients

**Theorem (law of the partial quotients).** The partial quotient $a_1$ has the distribution

$$
\mu(a_1=k)=\frac1{\log2}\log\Bigl(1+\frac1{k(k+2)}\Bigr)=\log_2\frac{(k+1)^2}{k(k+2)}, \qquad k \ge1,
$$

so that $\mu(a_1=1)=\log_2\frac43=0.41504\ldots$ and the distribution of $a_n$ converges to the same law; the mean of $a_1$ is infinite, $\int a_1\,d\mu=\infty$, because the tail is $\mu(a_1=k)\sim\frac1{k^2\log2}$.

*Proof.* The set $\{a_1=k\}$ is the interval $(\frac{1}{k+1},\frac1k]$, whose Gauss measure is $\frac{1}{\log2}\log\frac{1+1/k}{1+1/(k+1)}=\frac1{\log2}\log\frac{(k+1)^2}{k(k+2)}$; the distribution of $a_n$ converges to the law of $a_1$ by the Gauss–Kuzmin theorem, and the divergence of the mean is the divergence of the harmonic tail. $\square$

**Theorem (law of large numbers and Lévy's constant).** For Lebesgue-almost every $x$,

$$
\frac1n\log q_n\to\frac{\pi^2}{12\log2}=1.186569\ldots,
$$

the **Lévy constant**, and in particular the denominators of the convergents grow like $e^{n\pi^2/(12\log2)}$.

*Proof.* The recursion for the denominators gives $\log q_n=\log q_0+\sum_{k=1}^n\log\frac{q_k}{q_{k-1}}$, and the ratios $\frac{q_{k}}{q_{k-1}}=a_k+\frac{q_{k-2}}{q_{k-1}}$ converge to the corresponding function of $T^{k}x$; since $\frac{q_{k-2}}{q_{k-1}}\in(0,1)$, the summand is $\log(a_k+\theta_k)$ and is not $\log a_k$, and the Birkhoff ergodic theorem applied to the natural extension, whose second coordinate carries the backward digits, gives the limit as the mean of $\log(1/T^{k}x)$ along the orbit, that is $\frac1{\log2}\int_0^1\frac{-\log x}{1+x}\,dx$, since the ratios $q_k/q_{k-1}$ and $1/T^kx$ differ by a bounded factor. The value is

$$
\frac{\pi^2}{12\log2}=1.186569\ldots,
$$

which is exactly half the measure-theoretic entropy $h(T)=\frac{\pi^2}{6\log2}=2.373138\ldots$ of the Gauss map; the identity $L=\frac12h(T)$ between the Lévy constant and the entropy is the arithmetic form of the relation between the entropy and the mean return time of the modular flow, established in the next section. $\square$

**Theorem (Khinchin's theorem; the geometric mean).** For Lebesgue-almost every $x$,

$$
(a_1a_2\cdots a_n)^{1/n}\to K_0=2.6854520010\ldots,
$$

the **Khinchin constant**. The theorem is the statement that the ergodic average of $\log a_n$ converges, and by the ergodicity of the Gauss measure its value is $\log K_0=\int\log a_1\,d\mu$; the integral is $0.987849\ldots$, obtained by summing the convergent series $\sum_k\log k\,\mu(a_1=k)$ (the partial sum up to $k=2\cdot10^6$ gives $0.987838$, and $e^{0.987838}=2.685422$, in agreement with $K_0=2.6854520\ldots$), and $K_0$ has no known closed form. The statement holds with the same constant for every measure absolutely continuous with respect to the Gauss measure.

**Theorem (central limit theorem; Heinrich).** For Lebesgue-almost every $x$ the normalised sums of the logarithms of the partial quotients satisfy

$$
\frac1{\sqrt n}\sum_{k=1}^n\bigl(\log a_k-\log K_0\bigr)\longrightarrow\mathcal N(0,\sigma^2)
$$

in distribution, with a finite variance $\sigma^2$ given by the Green–Kubo sum $\sum_{k\in\mathbb{Z}}\operatorname{cov}(\log a_1,\log a_{k+1})$ of the stationary sequence of digits, finite because the correlations decay exponentially by the spectral gap; the result is proved by the martingale approximation of the sums, and it shows that the partial quotients, though not independent, obey the classical limit theorems with computable constants. The theorem and its refinements are instances of the general limit theory of the ergodic sums of a stationary process: the convergence of the normalised sums is the content of the central limit theorem and of the law of large numbers for the process of the digits, whose general form is that of *Laws of Large Numbers and the Central Limit Theorem*.

### Diophantine Approximation

**Theorem (Khinchin's approximation theorem).** Let $\psi:(0,\infty)\to(0,\infty)$ be decreasing. Then for Lebesgue-almost every $x$ the inequality

$$
\Bigl|x-\frac pq\Bigr|<\frac{\psi(q)}{q}
$$

has finitely many solutions in the rationals $\frac pq$ when $\sum_q\frac{\psi(q)}{q}<\infty$, and infinitely many when $\sum_q\frac{\psi(q)}{q}=\infty$; the function $\frac{\psi(q)}{q}$ is decreasing, so the second case is Khinchin's divergence theorem applied to it, and the first case follows from the Borel–Cantelli lemma and the estimate $\sum_q\frac{2\psi(q)}{q}$ for the measure of the approximable set. The threshold exponent $2$ in $|x-\frac pq|<q^{-2}$ is the statement that almost every $x$ has only finitely many approximations with exponent $2+\epsilon$, for every $\epsilon>0$.

**Theorem (Lagrange; Jarník).** A real $x$ is **badly approximable** — there is $c>0$ with $|x-\frac pq|>\frac{c}{q^2}$ for all rationals $\frac pq$ — if and only if its partial quotients are bounded; the set of the badly approximable numbers has Lebesgue measure zero and Hausdorff dimension $1$, by the theorem of Jarník. More generally the set of the $x$ whose partial quotients are bounded by $M$ has Hausdorff dimension tending to $1$ as $M\to\infty$, and the dimension of the set of the $x$ with a prescribed growth of the partial quotients is computed by the general Besicovitch–Eggleston theory of the digit restrictions.

## Homogeneous Dynamics and the Modular Flow

### The Modular Surface

**Definition.** The **modular surface** is the quotient $M=\mathbb{H}/SL(2,\mathbb{Z})$ of the hyperbolic plane by the modular group, a finite-volume noncompact hyperbolic surface with a cusp; the **modular flow** is the geodesic flow of the hyperbolic metric on $M$, acting on the unit tangent bundle $SM$, and the **continued fraction map** arises as the return map of the flow to a suitable cross-section: the geodesics that return to the cross-section are coded by the continued fraction expansion of their endpoint, and the successive return times of the flow to the cross-section are $2\log q_n$, so that the partial quotients are the itinerary of the geodesic and the denominators $q_n$ carry its return times.

**Theorem (Artin; Series).** The geodesic flow on the modular surface is a cross-section-suspension of the Gauss map: the return map of the flow to the cross-section is conjugate to the Gauss map, the return time function is $2\log(1/x)$ up to an additive constant, and the natural extension of the Gauss map is the return map to the cross-section of the two-dimensional extension of the flow. Consequently the ergodicity of the modular flow, the mixing, and the equidistribution of its periodic orbits, are equivalent to the corresponding properties of the Gauss map. Since the mean of $\log(1/x)$ under $\mu$ is the Lévy constant $\frac{\pi^2}{12\log2}$, the mean return time is twice it, namely the entropy $\frac{\pi^2}{6\log2}$ of the Gauss map, and Abramov's formula $h_{\mathrm{flow}}=h(T)/\bar\tau$ shows that the entropy of the flow is $1$ in this normalisation.

*Proof (sketch).* The strongly stable and strongly unstable manifolds of the modular flow are the horocycles; the cross-section is a set of horocycle arcs, and the return map is computed by the action of the modular group on the endpoints, which reproduces the recursion of the continued fraction algorithm. $\square$

**Theorem (ergodicity and equidistribution of the modular flow).** The modular geodesic flow is ergodic and mixing with respect to the Liouville measure, its periodic orbits equidistribute, and its closed geodesics are in bijection with the conjugacy classes of hyperbolic elements of $SL(2,\mathbb{Z})$, hence with the periodic continued fractions; the distribution of the closed geodesics and the asymptotics of their counting function are governed by the equidistribution theory of *Homogeneous Dynamics*, *Ratner's Theorems* and *Equidistribution*, of which the modular case is the simplest instance. The ergodicity and the mixing of the geodesic flow of a hyperbolic surface are those, and the counting of the closed geodesics by the trace formula is the arithmetic input of the *Lattices in Lie Groups* and the analytic number theory of the corpus.

## Further Arithmetic Systems

### Rotations and the Three-Distance Theorem

**Theorem (three-distance theorem; Steinhaus).** Let $\alpha$ be irrational and let $\{k\alpha\}$, $k=1,\dots,n$, be the first $n$ multiples of $\alpha$ on the circle. Then the $n$ points divide the circle into $n+1$ intervals whose lengths take at most three distinct values, and the lengths are determined by the continued fraction expansion of $\alpha$; the result is the combinatorial form of the equidistribution of the rotation, and the return times of the rotation to an interval are the Sturmian sequences of *Symbolic Dynamics*.

**Theorem (Furstenberg).** Let $X \subseteq\mathbb{T}^1$ be a closed set invariant under both $x\mapsto2x$ and $x\mapsto3x\pmod1$. Then $X$ is either finite or the whole circle. The theorem is the prototype of the rigidity results for the semigroup generated by two multiplicatively independent endomorphisms, and its proofs and generalisations belong to the ergodic theory of group actions and to the homogeneous dynamics of *Ergodic Theory of Group Actions* and *Homogeneous Dynamics*.

### The β-Shifts and the Expansions

**Example (the $\beta$-transformation).** For $\beta>1$ the **$\beta$-transformation** is $x\mapsto\beta x\bmod1$ on $[0,1)$, and the $\beta$-expansion of $x$ is the sequence of the integer parts of the iterates; the associated **$\beta$-shift** of *Symbolic Dynamics* is the closure of the set of the expansions, its topological entropy is $\log\beta$, and it is sofic when $\beta$ is a Parry number, that is, when the $\beta$-expansion of $1$ is eventually periodic; conversely the soficity forces $\beta$ to be a Perron number. The $\beta$-transformation is the natural generalisation of the doubling map $x\mapsto2x\bmod1$, and the arithmetic of the expansions — the greedy algorithm, the admissibility of the digit strings and the Pisot and Salem numbers — is the number-theoretic counterpart of the entropy formula.

**Example (the Collatz map).** The **Collatz map** is $C(n)=\frac n2$ for even $n$ and $C(n)=\frac{3n+1}{2}$ for odd $n$, acting on the positive integers; its conjectural behaviour is that every orbit reaches the cycle $1\to2\to1$, and the problem is open. The map is an arithmetic dynamical system with a known invariant measure structure only conjecturally, and the partial results — the almost-sure boundedness of the normalised orbits, and the density of the set of the points with a finite orbit — are proved by the methods of the measure-theoretic dynamics applied to the conjugating map to the $2$-adic integers, which exhibits the Collatz map as a piecewise translation. The problem is stated here as the standard open problem of the arithmetic dynamics; the $2$-adic conjugation used to state it is an instance of the local-field analysis of the corpus.

## Summary

The **Gauss map** $T(x)=\{1/x\}$ generates the continued fraction expansion $x=[0;a_1,a_2,\dots]$; it preserves the **Gauss measure** $d\mu=\frac{dx}{(1+x)\log2}$, which is ergodic and is the unique absolutely continuous invariant measure, and the **Gauss–Kuzmin theorem** states that $\mu(T^{-n}A)\to\mu(A)$ exponentially, with the **Gauss–Kuzmin–Wirsing operator** $\mathcal Pf(x)=\sum_k\frac{1}{(x+k)^2}f(\frac1{x+k})$ supplying the spectral gap and the second eigenvalue $\lambda_2=-0.303663\ldots$; the natural extension $\mathcal T(x,y)=(Tx,\frac{1}{a(x)+y})$ on $[0,1]^2$ with density $\frac{1}{\log2}(1+xy)^{-2}$ makes the map invertible and Bernoulli, and gives the exponential decay of correlations. The partial quotients obey the law $\mu(a_1=k)=\log_2\frac{(k+1)^2}{k(k+2)}$ with $\mu(a_1=1)=0.41504\ldots$ and infinite mean; the **Lévy constant** $\frac1n\log q_n\to\frac{\pi^2}{12\log2}=1.186569\ldots$ gives the growth of the denominators, the **Khinchin constant** $K_0=2.6854520\ldots$ is the almost-sure geometric mean of the digits, and a **central limit theorem** holds for the logarithms of the digits. **Khinchin's approximation theorem** decides the divergence and convergence of the approximations $|x-\frac pq|<\frac{\psi(q)}{q}$, and the **badly approximable** numbers are exactly those with bounded partial quotients, with Hausdorff dimension $1$ by the theorem of **Jarník**.

The **modular surface** $\mathbb{H}/SL(2,\mathbb{Z})$ and its geodesic flow place the continued fractions in homogeneous dynamics: by the theorems of **Artin** and **Series** the return map of the modular flow to a cross-section is the Gauss map, so the ergodicity, the mixing and the equidistribution of the flow are equivalent to the properties of the arithmetic map, and the mean return time of the flow to the cross-section is twice the Lévy constant, namely the entropy of the Gauss map; the closed geodesics correspond to the periodic continued fractions. The **three-distance theorem** of Steinhaus describes the combinatorial structure of the rotations, **Furstenberg's theorem** gives the rigidity of the closed sets invariant under $x\mapsto2x$ and $x\mapsto3x$, and the **$\beta$-shifts** realise the non-integer expansions with entropy $\log\beta$. The **Collatz map** is the standard open problem of the arithmetic dynamics. Throughout, the ergodic theory is that of *Ergodic Theory*, the symbolic models that of *Symbolic Dynamics*, the homogeneous dynamics that of *Homogeneous Dynamics* and *Ratner's Theorems*, and the arithmetic of the continued fractions of the rationals that of Part V .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T(x)=\{1/x\}$ | Gauss map |
| $a_n$, $[0;a_1,a_2,\dots]$ | partial quotients and continued fraction expansion |
| $p_n/q_n$, $q_n$ | convergents and their denominators |
| $\mu$, $\frac{1}{(1+x)\log2}$ | Gauss measure and Gauss density |
| $\mathcal P$ | Gauss–Kuzmin–Wirsing operator |
| $\mathcal T$, $\bar\mu$ | natural extension of the Gauss map and its invariant measure |
| $\lambda_2$ | Gauss–Kuzmin–Wirsing constant $-0.303663\ldots$ |
| $\frac{\pi^2}{12\log2}$ | Lévy constant $1.186569\ldots$ |
| $K_0$ | Khinchin constant $2.6854520\ldots$ |
| $\mathbb{H}$, $SL(2,\mathbb{Z})$ | hyperbolic plane, modular group |
| $M=\mathbb{H}/SL(2,\mathbb{Z})$ | modular surface |
| $SM$ | unit tangent bundle of the modular surface |
| $\beta$ | base of the $\beta$-transformation |
| $C$ | Collatz map |



## Further Reading

- Carl F. Gauss, *Werke*, vol. 10, part 1 (Teubner, 1917), for the original computation of the invariant measure of the continued fraction map.
- Rodion O. Kuzmin, "On a problem of Gauss", *Doklady Akademii Nauk SSSR* (1928), 375–380, and Eduard Wirsing, "On the theorem of Gauss–Kuzmin–Lévy and a Frobenius-type theorem for function spaces", *Acta Arithmetica* 24 (1974), 507–528, for the Gauss–Kuzmin theorem and its rate.
- Dieter H. Mayer, "On the thermodynamic formalism for the Gauss map", *Communications in Mathematical Physics* 130 (1990), 311–333, for the spectral gap and the value $\lambda_2=-0.303663\ldots$.
- Aleksandr Ya. Khinchin, *Continued Fractions* (University of Chicago Press, 1964), for the metric theory of the continued fractions and the constant $K_0$.
- Patrick Billingsley, *Ergodic Theory and Information* (Wiley, 1965), for the limit theorems for the partial quotients and the Lévy constant.
- Wolfgang Heinrich, "Rates of convergence in stable limit theorems for sums of exponentially $\psi$-mixing random variables with an application to metric theory of continued fractions", *Mathematische Nachrichten* 131 (1987), 149–165, for the central limit theorem for the logarithms of the partial quotients, with rates.
- Vojtěch Jarník, "Zur metrischen Theorie der diophantischen Approximationen", *Prace Matematyczno-Fizyczne* 36 (1928–1929), 91–106, for the dimension of the badly approximable numbers.
- Emil Artin, "Ein mechanisches System mit quasiergodischen Bahnen", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* 3 (1924), 170–175, and Caroline Series, "The modular surface and continued fractions", *Journal of the London Mathematical Society* 31 (1985), 69–80, for the coding of the modular geodesic flow by the continued fractions.
- Harry Furstenberg, "Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation", *Mathematical Systems Theory* 1 (1967), 1–49, for the rigidity of the $\times2$ and $\times3$ orbits.
- Jeffrey C. Lagarias, ed., *The Ultimate Challenge: The $3x+1$ Problem* (American Mathematical Society, 2010), for the state of the Collatz problem and its $2$-adic conjugation.
- Marius Iosifescu and Cor Kraaikamp, *Metrical Theory of Continued Fractions* (Kluwer, 2002), for the systematic account of the statistics of the continued fractions and the limit theorems.
