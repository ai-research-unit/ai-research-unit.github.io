
# __Harmonic Analysis on Groups__

## Introduction

Harmonic analysis on a group is the theory of the decomposition of a function on the group into its group-theoretic frequencies, and it is the analytic reading of the duality theory of Part II. For a locally compact abelian group $G$ the frequencies are the **characters** — the continuous homomorphisms $G \to S^1$ — and they form the Pontryagin dual $G^\vee$, itself a locally compact abelian group. The **Fourier transform** carries an integrable function on $G$ to a function on $G^\vee$, convolution of functions becomes pointwise multiplication of transforms, and the pair (inversion theorem, Plancherel theorem) says that the transform is, on the square-integrable functions, an isometry onto its image. Every one of the classical transforms — the Fourier transform on the line, the Fourier series on the circle, the discrete Fourier transform on a finite cyclic group — is one instance of this single construction, and the reason it is one instance is Pontryagin duality.

This article develops the general theory for a locally compact abelian group and records the obstruction that appears as soon as the group is non-abelian. It fixes the notation for the whole harmonic-analysis block of the category. The further development — the compact case, the Peter–Weyl theorem, the convolution algebra, the non-commutative theory and the Plancherel theorem — is carried by the five other articles, and the per-system transforms are Part V's.

Three boundaries are held exactly, and they are the reason the article says as little about representations as it does.

- The **representation theory** of locally compact groups — unitary representations, equivalences, irreducibility, intertwiners, induced representations, Mackey theory, the type classification, property (T) — is the subject of Part II, in *Representation Theory of Locally Compact Groups*, *Induced Representations of Locally Compact Groups*, *Mackey Theory* and *Type I Groups*. What belongs here is the *harmonic analysis*: the spaces $L^p(G)$, the transform on them, the convolution algebra $L^1(G)$ and its completions, and the decomposition theorems for $L^2(G)$.
- The **Haar measure** and the modular function are constructed in Part II, in *Locally Compact Groups and Haar Measure*; the general measure theory — $\sigma$-algebras, the integral, the $L^p$ spaces, Fubini–Tonelli, the Radon–Nikodym theorem — is *Measure Theory and Integration*, and the comparison of the various modes of convergence is *Modes of Convergence*, both in the Foundations slot of this Part. The functional analysis — Hilbert spaces, orthonormal bases, the spectral theorem, the Riesz representation theorem — is standard and is quoted as it is used, its systematic development in this Part belonging to the laterin the Analysis on Linear Spaces slot. The Euclidean transform that the additive groups of the number systems carry is *Fourier Analysis on Euclidean Spaces*.
- The **per-system** transforms — the Fourier series of the circle, the discrete transform of a finite abelian group, the transform of the $p$-adic line, and their hypercomplex relatives — are Part V's,and the other articles of the harmonic-analysis slots. This article writes the general theory once, and those articles instantiate it.

Throughout, $G$ is a locally compact Hausdorff group, written additively when abelian and multiplicatively otherwise, with identity $e$; $dx$ is a left Haar measure, $\Delta$ the modular function, and $G$ is **unimodular** when $\Delta \equiv 1$. The base ring $R$ is commutative with $1 \neq 0$ and $F$, $K$ are fields, as in the corpus conventions. The circle is $S^1 = \{z \in \mathbb{C} : |z| = 1\} = \mathbb{R}/\mathbb{Z}$ and $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$. The abelian dual is written $G^\vee$ and the set of equivalence classes of irreducible unitary representations of a general group is written $\operatorname{Irr}(G)$; the hat is not used for a dual, being reserved in this corpus for completions. No physics is invoked.

## Characters and the Dual Group

**Definition.** Let $G$ be a locally compact abelian group. A **character** of $G$ is a continuous homomorphism $\chi : G \to S^1$. The **dual group** $G^\vee$ is the set of characters with the pointwise product and the compact-open topology.

The dual group, its functoriality and its topology, the exchange of compactness and discreteness, and the duality theorem are the subject of *Abelian Topological Groups* and *Pontryagin Duality*, and are used here as established facts. Three of them are quoted repeatedly.

**Theorem (Pontryagin).** For every locally compact abelian group $G$ the evaluation map $\iota_G : G \to G^{\vee\vee}$, $\iota_G(x)(\chi) = \chi(x)$, is an isomorphism of topological groups. The assignment $G \mapsto G^\vee$ is a contravariant equivalence between the category of locally compact abelian groups and its opposite, exchanging compact with discrete groups.

**Theorem (topology of the dual).** $G^\vee$ is locally compact abelian and the evaluation pairing $G \times G^\vee \to S^1$ is continuous. If $G$ is compact then $G^\vee$ is discrete; if $G$ is discrete then $G^\vee$ is compact.

**Example (the standard duals).** $\mathbb{R}^\vee \cong \mathbb{R}$ through $\chi_\xi(x) = e^{2\pi i \xi x}$; $(S^1)^\vee \cong \mathbb{Z}$; $\mathbb{Z}^\vee \cong S^1$; $T^n{}^\vee \cong \mathbb{Z}^n$; $\mathbb{Q}_p{}^\vee \cong \mathbb{Q}_p$ and $\mathbb{Z}_p{}^\vee \cong \mu_{p^\infty}$. For a finite abelian group $G$ the dual has the same order as $G$, and after a choice of roots of unity $G \cong G^\vee$, non-canonically.

The characters of the additive groups of the number systems are the frequencies of the per-system transforms of Part V, and the identifications above are the ones those articles use.

## The Fourier Transform

### Definition and Elementary Properties

**Definition.** Let $G$ be a locally compact abelian group with Haar measure $dx$. For $f \in L^1(G)$ the **Fourier transform** is the function

$$
\hat f(\chi) = \int_G f(x)\,\overline{\chi(x)}\,dx, \qquad \chi \in G^\vee ,
$$

and for a finite positive measure $\mu$ on $G$ the **Fourier–Stieltjes transform** is $\hat\mu(\chi) = \int_G \overline{\chi(x)}\,d\mu(x)$. When $G$ is written additively and identified with $\mathbb{R}^n$ this is the classical transform with the normalisation of *Fourier Analysis on Euclidean Spaces*: for $G = \mathbb{R}^n$ and $\chi_\xi(x) = e^{2\pi i\langle\xi, x\rangle}$,

$$
\hat f(\xi) = \int_{\mathbb{R}^n} f(x)\,e^{-2\pi i\langle\xi,x\rangle}\,dx ,
$$

with no factor of $(2\pi)^{n/2}$; the $2\pi$ is carried by the character. The convention is the one of *Pontryagin Duality*, §Characters and the Dual Group, and it is held for the whole category.

**Theorem (elementary properties).** For $f, g \in L^1(G)$, $\alpha, \beta \in \mathbb{C}$ and $x_0 \in G$:

**(a)** $\widehat{\alpha f + \beta g} = \alpha \hat f + \beta \hat g$, and $\|\hat f\|_\infty \leq \|f\|_1$;

**(b)** $\hat f$ is uniformly continuous on $G^\vee$ and vanishes at infinity: $\hat f \in C_0(G^\vee)$, the **Riemann–Lebesgue lemma**;

**(c)** if $f_{x_0}(x) = f(x - x_0)$ then $\widehat{f_{x_0}}(\chi) = \overline{\chi(x_0)}\,\hat f(\chi)$, and if $f^\chi(x) = \chi(x) f(x)$ then $\widehat{f^\chi} = \hat f(\,\cdot - \chi)$;

**(d)** $\widehat{\bar f}(\chi) = \overline{\hat f(-\chi)}$, where $\bar f(x) = \overline{f(x)}$.

**Proof.** (a) is linearity of the integral and $|\hat f(\chi)| \leq \int |f|$. (b) The continuity of the integral under translation of the variable in the group is the continuity of translation in $L^1(G)$: $\|f_{x} - f\|_1 \to 0$ as $x \to 0$, which follows from the density of $C_c(G)$ in $L^1(G)$ and the uniform continuity of a compactly supported function. Uniform continuity of $\hat f$ follows, since $|\hat f(\chi) - \hat f(\chi')| \leq \| f - f \cdot (\chi' \bar\chi) \|_1$ and $\chi'\bar\chi \to 1$ uniformly on compacta. The vanishing at infinity reduces, by density of $C_c(G)$ in $L^1(G)$, to the case of a continuous compactly supported $f$, where $\hat f$ is the Fourier transform of a compactly supported function; if the support of $f$ has small measure and $\|f\|_\infty$ is bounded, then $|\hat f(\chi)|$ is small uniformly in $\chi$ unless $\chi$ is near $1$, and off a compact set of characters the oscillation kills the integral. The standard proof is in *Fourier Analysis on Euclidean Spaces* for the case $G = \mathbb{R}^n$ and in the references below for the general case; it is quoted as standard. (c) and (d) are changes of variable. $\square$

**Corollary (the transform of a dilation and of a derivative).** On $G = \mathbb{R}$ one has $\widehat{f(ax)}(\xi) = |a|^{-1}\hat f(\xi/a)$ for $a \neq 0$, and if $f$ is absolutely continuous with $f' \in L^1$ then $\widehat{f'}(\xi) = 2\pi i \xi \hat f(\xi)$. On $\mathbb{R}^n$ the corresponding statements hold componentwise, and differentiation is turned into multiplication by the character's infinitesimal generator.

### Convolution and the Convolution Theorem

**Definition.** For $f, g \in L^1(G)$ the **convolution** is

$$
(f * g)(x) = \int_G f(y)\,g(y^{-1}x)\,dy ,
$$

the integral being with respect to the left Haar measure of *Locally Compact Groups and Haar Measure*.

**Proposition.** The convolution is defined for almost every $x$, belongs to $L^1(G)$, and satisfies **Young's inequality**

$$
\|f * g\|_1 \leq \|f\|_1\,\|g\|_1 .
$$

Associativity $(f*g)*h = f*(g*h)$ holds, so $L^1(G)$ is a Banach algebra under convolution; it is commutative exactly when $G$ is abelian.

**Proof.** By Tonelli's theorem, the double integral of $|f(y)||g(y^{-1}x)|$ over $G \times G$ is $\|f\|_1\|g\|_1 < \infty$, so $f*g$ is defined a.e. and integrable, with the bound; the estimate is the definition of the $L^1$ norm together with the left invariance of $dy$. Associativity is Fubini's theorem applied to the three-variable integral, and the change of variables is left-invariant. If $G$ is abelian, the substitution $y \mapsto xy^{-1}$ gives $f*g = g*f$; if $G$ is not abelian, choose $f$, $g$ supported near non-commuting elements and test, as in the example of the next paragraph. $\square$

**Example (convolution on $\mathbb{Z}$).** On the discrete group $\mathbb{Z}$ with counting measure, $f * g(n) = \sum_{m \in \mathbb{Z}} f(m) g(n - m)$ is the Cauchy product of sequences, and $L^1(\mathbb{Z}) = \ell^1(\mathbb{Z})$ is the Banach algebra of absolutely convergent Fourier series under multiplication.

**Example (convolution on a non-abelian group).** Let $G = S_3$ with the normalised counting measure and let $f$ and $g$ be the indicator functions of the transposition $(12)$ and the cycle $(123)$ divided by $|G|$. Then $(f*g)(x) = \frac{1}{36}\#\{y : y = (12),\ y^{-1}x = (123)\}$, which is nonzero only at $x = (12)(123)$ while $(g*f)$ is nonzero only at $(123)(12)$, and these two products differ; hence $L^1(S_3)$ is not commutative. Convolution on a finite group is the multiplication of the group algebra under the identification of $L^1(G)$ with $\mathbb{C}[G]$ normalised by the counting measure.

**Theorem (convolution theorem).** For $f, g \in L^1(G)$,

$$
\widehat{f * g}(\chi) = \hat f(\chi)\,\hat g(\chi), \qquad \chi \in G^\vee .
$$

*Proof.* Substituting $x = yz$ in the defining integral and using the left invariance of $dz$ and the multiplicativity $\chi(yz) = \chi(y)\chi(z)$,

$$
\widehat{f*g}(\chi) = \int_G \int_G f(y)g(z)\,\overline{\chi(y)\chi(z)}\,dz\,dy = \hat f(\chi)\hat g(\chi). \qquad \square
$$

The convolution theorem is the reason the transform is useful: it converts the non-local operation of convolution into pointwise multiplication, and it is the exact sense in which the transform is a homomorphism of the convolution algebra.

### The Inversion and Plancherel Theorems

The transform of an $L^1$ function need not be integrable, so inversion requires a hypothesis on $\hat f$. The dual group carries a Haar measure chosen to make the pair of formulas below hold; its normalisation is fixed in the next subsection.

**Theorem (inversion).** There is a Haar measure $d\chi$ on $G^\vee$ such that for every $f \in L^1(G)$ with $\hat f \in L^1(G^\vee)$ the function $f$ agrees almost everywhere with the continuous function

$$
f(x) = \int_{G^\vee} \hat f(\chi)\,\chi(x)\,d\chi .
$$

In particular $f$ is equal a.e. to a function vanishing at infinity.

**Proof sketch.** The proof is the standard approximate-identity argument. Choose a net $(u_\alpha)$ of nonnegative continuous functions of integral $1$ supported in shrinking neighbourhoods of $e$; then $f * u_\alpha \to f$ in $L^1(G)$ and, for continuous $f$, uniformly on compacta. On the Fourier side $\widehat{f * u_\alpha} = \hat f\hat u_\alpha$, and the integral $\int_{G^\vee}\hat f(\chi)\hat u_\alpha(\chi)\chi(x)\,d\chi$ is computed by Fubini as $(f * u_\alpha)(x)$ for a suitable choice of $d\chi$; letting the neighbourhoods shrink gives the result. The argument is the one given in *Fourier Analysis on Euclidean Spaces* for $G = \mathbb{R}^n$ and in the references below in general. $\square$

**Theorem (Plancherel).** Let $d\chi$ be the dual Haar measure of the inversion theorem. The Fourier transform is an isometry of the dense subspace $L^1(G) \cap L^2(G)$ of $L^2(G)$ into $L^2(G^\vee)$,

$$
\int_G |f(x)|^2\,dx = \int_{G^\vee} |\hat f(\chi)|^2\,d\chi ,
$$

and it extends uniquely to a unitary equivalence of Hilbert spaces $\mathcal{F} : L^2(G) \to L^2(G^\vee)$.

**Proof sketch.** For $f \in L^1 \cap L^2$ put $h = f * f^*$, where $f^*(x) = \overline{f(-x)}$ on an abelian group, so that $h \in L^1(G)$ and, by the convolution theorem, $\hat h = |\hat f|^2 \geq 0$ and $\hat h \in L^1(G^\vee)$ because $\hat f \in L^2 \cap L^\infty$ forces $|\hat f|^2 \in L^1$. The inversion theorem applies to $h$ and gives $h(0) = \int_{G^\vee}|\hat f|^2\,d\chi$; but $h(0) = \int_G f(x)\overline{f(x)}\,dx = \|f\|_2^2$. This is the identity. The extension to all of $L^2(G)$ follows because $L^1 \cap L^2$ is dense, and the extension is onto because its image is closed and contains the transform of an approximate identity, which converges weakly to $1$; surjectivity is also a consequence of the inversion formula applied to a dense set. $\square$

**Remark (the two theorems are one).** Inversion and Plancherel are the two halves of the statement that the transform is an isomorphism of the group algebra of $G$ together with its $L^2$ structure. Inversion is the statement at the level of functions, Plancherel the statement at the level of the inner product; for a compact group both are contained in the Peter–Weyl theorem, and for the abelian case they are the content of the two theorems above.

### The Dual Haar Measure

The inversion theorem does not determine $d\chi$ alone but only after $dx$ is fixed, and the pair is fixed by demanding the two formulas. The rule is the following.

**Proposition (normalisation).** Let $dx$ be a fixed Haar measure on $G$. There is a unique Haar measure $d\chi$ on $G^\vee$ for which inversion and Plancherel hold. If $dx$ is replaced by $c\,dx$, $c > 0$, then $d\chi$ is replaced by $c^{-1}d\chi$, and the product of the two total masses is $1$ whenever both groups are compact.

**Example.** On $\mathbb{R}$ with $dx$ Lebesgue measure, the dual is $\mathbb{R}$ with $d\xi$ Lebesgue measure and $\chi_\xi(x) = e^{2\pi i \xi x}$; the inversion formula $\hat f(\xi) = \int f(x)e^{-2\pi i\xi x}dx$, $f(x) = \int \hat f(\xi)e^{2\pi i\xi x}d\xi$ holds. On $S^1$ with the normalised measure $d\theta$ of total mass $1$, the dual is $\mathbb{Z}$ with counting measure: $\hat f(n) = \int_0^1 f(\theta)e^{-2\pi i n\theta}d\theta$ and $f(\theta) = \sum_{n\in\mathbb{Z}}\hat f(n)e^{2\pi i n\theta}$. On a finite abelian group with the normalised counting measure $|G|^{-1}\sum_x$, the dual carries counting measure: $\hat f(\chi) = |G|^{-1}\sum_x f(x)\overline{\chi(x)}$, $f(x) = \sum_\chi \hat f(\chi)\chi(x)$, the discrete Fourier transform and its inversion. On a compact group with normalised Haar measure, the dual is discrete with counting measure; on a discrete group with counting measure, the dual is compact with Haar measure of total mass $1$. These are the four faces of one statement, and they are worked out system by system in the harmonic-analysis slots of Part V.

## The Algebra of the Transform

### The Transform as an Algebra Homomorphism

The convolution theorem says that $\mathcal{F} : (L^1(G), *) \to (C_0(G^\vee), \cdot)$ is an algebra homomorphism; invertibility properties are read from it.

**Theorem.** The Fourier transform is an injective homomorphism of the commutative Banach algebra $L^1(G)$ onto a dense subalgebra of $C_0(G^\vee)$; the image separates the points of $G^\vee$ and does not vanish identically at any point. Its **Gelfand spectrum**, the set of nonzero complex homomorphisms $L^1(G) \to \mathbb{C}$ with the weak-$*$ topology, is homeomorphic to $G^\vee$, the homomorphism corresponding to $\chi$ being $f \mapsto \hat f(\chi)$.

**Proof.** The homomorphism property is the convolution theorem; injectivity is the statement that a function whose transform vanishes identically is zero, which follows from inversion applied to $f * u$ for an approximate identity $u$, or from the equality of the Fourier–Stieltjes transforms of $f\,dx$ and $0$; the density and separation statements are the Riemann–Lebesgue lemma and the ability of characters to separate points of $G^\vee$. The Gelfand spectrum of a commutative Banach algebra with involution is the space of characters, and the characters of $L^1(G)$ are exactly the maps $f \mapsto \hat f(\chi)$: a complex homomorphism $h$ is bounded with $\|h\| \leq 1$, and it determines a bounded representation of $L^1(G)$ on $\mathbb{C}$, which by the correspondence below is a one-dimensional unitary representation of $G$, that is, a character $\chi$ with $h(f) = \hat f(\chi)$. $\square$

**Corollary (Gelfand–Raĭkov).** A locally compact abelian group is determined up to topological isomorphism by its convolution algebra $L^1(G)$, and the group can be recovered as the Gelfand spectrum of $L^1(G)$. Consequently the characters separate the points of $G$.

**Remark (the $C^*$-completion).** The involution $f^*(x) = \overline{f(-x)}$ makes $L^1(G)$ a Banach $*$-algebra, and the transform is a $*$-homomorphism into $C_0(G^\vee)$ with $\widehat{f^*}(\chi) = \overline{\hat f(\chi)}$. The completion of $L^1(G)$ in the norm $\|f\|_{C^*} = \sup\{\|\hat f\|_\infty\}$ is the **group $\mathrm{C}^*$-algebra** $C^*(G)$, and the Gelfand–Naimark theorem gives $C^*(G) \cong C_0(G^\vee)$ for abelian $G$; the transform is that isomorphism. This is the commutative case of the operator-algebraic picture, and the non-abelian replacement is treated andwith the operator algebras themselves in *Operator Algebras*.

### Positive-Definite Functions and Bochner's Theorem

**Definition.** A function $\varphi : G \to \mathbb{C}$ is **of positive type** (or positive definite) if for every finite family $x_1, \dots, x_n \in G$ and $c_1, \dots, c_n \in \mathbb{C}$,

$$
\sum_{i,j=1}^n c_i\,\overline{c_j}\,\varphi(x_j - x_i) \geq 0 .
$$

**Theorem (Bochner).** A continuous function $\varphi : G \to \mathbb{C}$ is of positive type if and only if it is the Fourier–Stieltjes transform of a finite positive measure $\mu$ on $G^\vee$,

$$
\varphi(x) = \int_{G^\vee} \chi(x)\,d\mu(\chi) .
$$

The measure is unique, and $\varphi(0) = \mu(G^\vee) = \|\mu\|$.

**Proof sketch.** If $\varphi$ is of positive type, the sesquilinear form on $C_c(G)$ given by $\langle f, g\rangle_\varphi = \int\int f(x)\overline{g(y)}\varphi(y-x)\,dx\,dy$ is positive semidefinite; completing and factoring gives a Hilbert space $H_\varphi$ on which $G$ acts unitarily by translation, and the vector $\xi = [\text{an approximate delta}]$ is cyclic. Since $G$ is abelian, the operators of translation commute and Fourier analysis of the commutative algebra they generate identifies the representation with a direct integral of characters; the spectral measure of $\xi$ is the measure $\mu$, and evaluation at $\xi$ gives the displayed formula. Conversely a Fourier–Stieltjes transform of a positive measure is of positive type because $\sum c_i\bar c_j\chi(x_j - x_i) = |\sum_i c_i\chi(x_i)|^2 \geq 0$ and integration preserves positivity. Uniqueness is the invertibility of the transform on measures. This is the standard Gelfand–Naimark–Segal construction; the version used here is in the references below. $\square$

**Corollary (Herglotz and the Wiener–Khinchin theorem).** On $\mathbb{Z}$ a positive-definite sequence is the sequence of Fourier coefficients of a positive measure on the circle; on $\mathbb{R}$ the autocorrelation $R(\tau) = \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^T f(t+\tau)\overline{f(t)}\,dt$ of a stationary square-integrable process has a positive spectral measure, and the transform of that measure is $R$. The probabilistic reading of Bochner's theorem is the spectral theory of stationary processes.

## The Standard Cases

### The Line and Euclidean Space

For $G = \mathbb{R}^n$ the theory is the classical one: $\hat f(\xi) = \int f(x)e^{-2\pi i\langle\xi,x\rangle}dx$, inversion holds for $f \in L^1$ with $\hat f \in L^1$, and Plancherel extends the transform to a unitary operator on $L^2(\mathbb{R}^n)$. The Schwartz space $\mathcal{S}(\mathbb{R}^n)$ is invariant, the transform interchanges multiplication by $x^\alpha$ with $(-2\pi i)^{|\alpha|}\partial^\alpha$ up to signs, and it extends to the tempered distributions. The theory is developed in *Fourier Analysis on Euclidean Spaces*, and the $n$-dimensional cases of the per-system articles are its restriction to the additive group of each algebra.

### The Circle, the Torus and the Integers

For $G = S^1$ with normalised Haar measure the transform is the map assigning to $f \in L^1(S^1)$ its **Fourier coefficients**

$$
\hat f(n) = \int_0^1 f(\theta)\,e^{-2\pi i n\theta}\,d\theta , \qquad n \in \mathbb{Z},
$$

and inversion says that the partial sums of $\sum_n \hat f(n)e^{2\pi i n\theta}$ converge to $f$ in $L^2$ and at every Lebesgue point; the Plancherel identity is Parseval's identity $\int_0^1|f|^2 = \sum_n|\hat f(n)|^2$. For $T^n$ the dual is $\mathbb{Z}^n$ and the transform is the multiple Fourier series indexed by $\mathbb{Z}^n$. For $G = \mathbb{Z}$ with counting measure, the transform is $\hat f(\theta) = \sum_{n\in\mathbb{Z}}f(n)e^{-2\pi i n\theta}$ on $S^1 = \mathbb{Z}^\vee$, inversion is the recovery of the sequence from its Fourier coefficients, and Plancherel is Parseval's identity for sequences. The pair $S^1 \leftrightarrow \mathbb{Z}$ is the exact statement that compactness and discreteness are exchanged by duality, and it is why the theory of Fourier series and the theory of Fourier transforms are the same theory.

### Finite Abelian Groups

For a finite abelian group with the normalised counting measure the transform is the **discrete Fourier transform**

$$
\hat f(\chi) = \frac{1}{|G|}\sum_{x\in G} f(x)\,\overline{\chi(x)} , \qquad f(x) = \sum_{\chi\in G^\vee}\hat f(\chi)\,\chi(x) ,
$$

and Plancherel reads $\sum_x|f(x)|^2 = |G|\sum_\chi|\hat f(\chi)|^2$ under the normalisations above. The transform identifies the convolution algebra $L^1(G) = \mathbb{C}[G]$ with $\mathbb{C}^{|G|}$, the algebra of functions on the dual with pointwise multiplication; by the Wedderburn–Artin theorem this is the decomposition of the group algebra of a finite abelian group into one-dimensional summands. The finite cyclic case is the transform read through the present theory.

### The $p$-adic Line

For $G = \mathbb{Q}_p$ the dual is $\mathbb{Q}_p$ through the standard additive character $\chi_\xi(x) = e^{2\pi i \{\xi x\}_p}$, where $\{\cdot\}_p$ is the fractional part with values in $\mathbb{Z}[1/p]/\mathbb{Z} \subset \mathbb{Q}/\mathbb{Z}$, and the dual Haar measure is normalised so that $\mathbb{Z}_p$ and its dual both have measure $1$. The transform is the $p$-adic Fourier transform, and its analysis — the radius of convergence, the role of the residue field, the analogue of the Schwartz class — is the subject andin the Analysis on Rings and Fields slot, together. The group-theoretic input is the present section, and it is the exact analogue of the real case.

## The Obstruction for Non-Abelian Groups

### Characters Do Not Suffice

Let $G$ be a locally compact group that is not abelian. The characters of $G$ — the continuous homomorphisms $G \to S^1$ — still exist, but they are few, because a character must be constant on the commutator subgroup $[G,G]$. For a perfect group, in particular, the only character is the trivial one. The characters therefore cannot separate the points of $G$ and cannot carry the decomposition of $L^2(G)$.

**Example (the symmetric group $S_3$).** The group $S_3$ of order $6$ has abelianisation $S_3/[S_3,S_3] \cong \mathbb{Z}/2$, so it has exactly two characters, the trivial one and the sign, whereas it has a third irreducible representation of dimension $2$ — the reflection representation on the subspace of $\mathbb{C}^3$ orthogonal to $(1,1,1)$, or equivalently the action on the three lines of a triangle. The two characters account for a two-dimensional subspace of the regular representation $\mathbb{C}[S_3]$, and the remaining four dimensions are the two copies of the two-dimensional representation. Since $1^2 + 1^2 + 2^2 = 6 = |S_3|$, the sum of squares of the dimensions has found the whole group algebra, but the two-dimensional summand is invisible to the characters as a *function* theory on a dual group: the dual is not a group.

The example shows exactly what fails. For an abelian group the irreducible unitary representations are the characters, they are one-dimensional, and their equivalence classes form the group $G^\vee$; the transform is scalar-valued and defined on a group. For a non-abelian group the irreducible unitary representations are typically higher-dimensional, their equivalence classes form the **unitary dual** $\operatorname{Irr}(G)$, which is a set and not a group, and the transform must be operator-valued. The convolution algebra $L^1(G)$ is non-commutative, has no Gelfand transform, and its representation theory is that of a non-commutative Banach $*$-algebra.

### The Matrix-Valued Transform

The general replacement is as follows; the statements are made precise in the other articles, and the representation theory they use is Part II's.

Let $G$ be unimodular and $\pi : G \to U(\mathcal{H}_\pi)$ an irreducible unitary representation. For $f \in L^1(G)$ put

$$
\hat f(\pi) = \int_G f(g)\,\pi(g)\,dg \in B(\mathcal{H}_\pi) ,
$$

an operator on the representation space, and for $u, v \in \mathcal{H}_\pi$ let $c^\pi_{u,v}(g) = \langle \pi(g)u, v\rangle$ be the **matrix coefficient**. Then the convolution theorem retains its form, $\widehat{f * g}(\pi) = \hat f(\pi)\hat g(\pi)$, with operator multiplication, and the transform is a non-commutative functional calculus on $L^1(G)$ whose values are operators. For a compact group the theory of the transform, the orthogonality relations and the inversion and Plancherel formulas are not covered here; for a general unimodular group of type I, the decomposition of $L^2(G)$ as a direct integral over $\operatorname{Irr}(G)$ and the Plancherel theorem arewith the operator-algebraic completions and the general theory. The class of groups for which this works well — the type I groups — is classified in Part II's *Type I Groups*, and the failure is exhibited there by the free group on two generators.

**Theorem (compact case, quoted).** If $G = K$ is compact, every irreducible unitary representation is finite-dimensional, every unitary representation is a direct sum of irreducibles, and the normalised matrix coefficients $\sqrt{d_\pi}\,c^\pi_{ij}$, with $d_\pi = \dim\mathcal{H}_\pi$, form an orthonormal basis of $L^2(K)$. This is the Peter–Weyl theorem; it is stated and proved with its consequences, and the associated Fourier inversion and Plancherel formul.

**Theorem (abelian case).** If $G$ is abelian, every irreducible unitary representation is one-dimensional, $\operatorname{Irr}(G) = G^\vee$, and the matrix-valued transform reduces to the scalar transform of the present article. This is the content of the proposition of *Representation Theory of Locally Compact Groups*, §The General Case and the Unitary Dual, that the unitary dual of an abelian group is its Pontryagin dual.

### The Per-System Transforms of Part V

The general theory above is instantiated, system by system, in the harmonic-analysis slots of Part V. The additive group of each number system is a locally compact abelian group, and the transform of that group, together with the extra structure the multiplication and the conjugation supply, is the subject of the corresponding article.

| System | Additive group | Harmonic analysis in Part V |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | the real transform |
| $\mathbb{C}$ | $\mathbb{R}^2$ | the complex transform |
| $\mathbb{D}$ | $\mathbb{R}^2$ | the split-complex transform |
| $\mathbb{D}'$ | $\mathbb{R}^2$ | the dual-number transform |
| $\mathbb{H}$ | $\mathbb{R}^4$ | the quaternion transform |
| $\mathbb{B}$ | $\mathbb{R}^8$ | the biquaternion transform |

The transform in each row is the transform of the additive group, which is why the several systems share one transform and differ only in the algebra in which convolution multiplies; this observation is made here, in the general theory; the per-system articles of Part V, among themtake it up and develop the consequences. The discrete and finite cases of the same construction are the transforms of the finite and discrete groups that those systems conta.

## Summary

For a locally compact abelian group $G$ the characters $\chi : G \to S^1$ form the dual group $G^\vee$ under pointwise multiplication with the compact-open topology, and Pontryagin duality identifies $G$ with $G^{\vee\vee}$ and exchanges compactness with discreteness. The Haar measure of Part II and the integration of Part III give the Fourier transform $\hat f(\chi) = \int_G f(x)\overline{\chi(x)}\,dx$, which is linear, bounded by $\|f\|_1$, maps $L^1(G)$ into $C_0(G^\vee)$ (Riemann–Lebesgue), and turns convolution into pointwise multiplication: $\widehat{f*g} = \hat f\hat g$. With the dual Haar measure normalised by the inversion formula $f(x) = \int_{G^\vee}\hat f(\chi)\chi(x)\,d\chi$, the transform is an algebra isomorphism of $L^1(G)$ onto a dense subalgebra of $C_0(G^\vee)$, its Gelfand spectrum is $G^\vee$, and it extends to a unitary equivalence of $L^2(G)$ with $L^2(G^\vee)$ (Plancherel). Positive-definite functions are exactly the Fourier–Stieltjes transforms of finite positive measures on the dual (Bochner).

The standard cases are the Fourier transform of $\mathbb{R}^n$, the Fourier series of the circle and the torus with dual $\mathbb{Z}^n$, the discrete transform of $\mathbb{Z}$ with dual $S^1$, the discrete Fourier transform of a finite abelian group with the Wedderburn decomposition of its group algebra, and the $p$-adic transform with the self-dual normalisation of $\mathbb{Q}_p$; all are one theorem, and the per-system transforms of Part V are its instances. The obstruction in the non-abelian case is that the characters are too few — $S_3$ has two of them and an additional two-dimensional irreducible representation — so the transform becomes operator-valued, indexed by the unitary dual $\operatorname{Irr}(G)$ rather than by a dual group, and the convolution algebra loses its Gelfand theory. The compact, general unimodular and operator-algebraic forms of the non-abelian theory are the next five articles of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$ | Locally compact Hausdorff group and its identity |
| $dx$, $\Delta$ | Left Haar measure and modular function (Part II) |
| unimodular | $\Delta \equiv 1$; left Haar measure is right-invariant |
| $S^1 = \mathbb{R}/\mathbb{Z}$ | The circle group |
| $\chi$, $G^\vee$ | Character $G \to S^1$; dual group with compact-open topology |
| $\mathbb{R}^\vee \cong \mathbb{R}$, $\chi_\xi(x) = e^{2\pi i\xi x}$ | Characters of $\mathbb{R}^n$ |
| $\operatorname{Irr}(G)$ | Unitary dual of a non-abelian group |
| $\hat f(\chi) = \int_G f(x)\overline{\chi(x)}\,dx$ | Fourier transform on an abelian group |
| $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$ | Operator-valued transform on a non-abelian group |
| $c^\pi_{u,v}(g) = \langle\pi(g)u,v\rangle$ | Matrix coefficient |
| $(f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy$ | Convolution |
| $f^*(x) = \overline{f(-x)}$ | Involution on $L^1(G)$ in the abelian case |
| $L^1(G)$, $C^*(G)$ | Convolution algebra and group $\mathrm{C}^*$-algebra |
| $C_0(G^\vee)$ | Continuous functions vanishing at infinity on the dual |
| $\|f\|_1$, $\|f\|_2$ | Norms of $L^1(G)$, $L^2(G)$ |
| positive type | $\sum_{i,j}c_i\overline{c_j}\varphi(x_j - x_i) \geq 0$ |
| $\mu$ on $G^\vee$ | Spectral measure of Bochner's theorem |
| $d\chi$ | Dual Haar measure, fixed by inversion |
| $T^n = \mathbb{R}^n/\mathbb{Z}^n$ | The $n$-torus |
| $\mathbb{Q}_p$, $\mathbb{Z}_p$ | $p$-adic line, self-dual, and its unit ball |







## Further Reading

- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962; reprinted Wiley, 1990), for the transform on locally compact abelian groups, its algebra and its applications.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* and *II* (Springer, 2nd ed. 1979, 1970), for the full theory of the transform, convolution and the dual group.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for a concise account of the transform and the Gelfand theory of $L^1(G)$.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the transform, the inversion and Plancherel theorems, and the compact and abelian cases.
- Nicolas Bourbaki, *Théories spectrales* (Springer, 2019; English translation *Spectral Theories*, 2023), for the spectral theory of commutative Banach algebras underlying the Gelfand transform.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the case $G = \mathbb{R}^n$ in detail.
- Mark A. Pinsky, *Introduction to Fourier Analysis and Wavelets* (Brooks/Cole, 2002), for the discrete and finite transforms as instances of the general theory.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
