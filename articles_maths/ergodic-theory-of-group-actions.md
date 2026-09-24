
# __Ergodic Theory of Group Actions__

## Introduction

Ergodic theory is the study of a group of measure-preserving transformations of a probability space, and the question it asks is how a typical orbit distributes itself in the space. When the group is $\mathbb{Z}$ the group acts through the iterates of one transformation, and the theory is that of a single map; when the group is $\mathbb{R}$ the action is a flow; for a general locally compact group the group itself becomes part of the apparatus, and the passage from a single transformation to an action is not a formal generalisation but a change of method. Two features appear that have no counterpart for a single map. The first is that the group carries an algebraic structure — a Følner sequence, an averaging procedure, a lattice, a unipotent element — and the theorems are obtained by exploiting that structure. The second is that the theory of a group action is a tool for the analysis of the group itself: the ergodicity of a translation on a torus is a statement about irrationality, and the ergodicity of a horocycle flow is a statement about lattices in a Lie group.

This article develops the group-action theory: the definitions of invariance, ergodicity and mixing for an action; the Koopman representation and the spectral reading of ergodicity; the mean and pointwise ergodic theorems in their Følner form for amenable groups; the Mautner phenomenon and the ergodicity and mixing theorems of Moore and Howe–Moore; orbit equivalence and the ratio ergodic theorem; and the examples — translations on tori, Bernoulli actions, algebraic and homogeneous actions, and the geodesic and horocycle flows.

Three boundaries are held exactly.

- The general measure-theoretic theory of a **single** measure-preserving transformation is the subject of another article of the category. That article develops the theory in the sharp form it takes for one map: Poincaré recurrence, the Birkhoff pointwise theorem and the von Neumann mean theorem with their proofs and maximal inequalities, the ergodic decomposition, Kolmogorov–Sinai entropy, Bernoulli shifts and the Ornstein isomorphism theorem. This article is the *group-action* theory. The two overlap at the von Neumann and Birkhoff theorems for $\mathbb{Z}$; both are stated here as standard mathematics, with their proofs in the cited literature, and the sharp form for a single map is not covered here. The division is stated again in the introduction.
- The general **measure theory** — measurable spaces, measures, the integral, the $L^p$ spaces, convergence almost everywhere, the Radon–Nikodym theorem — belongs to *Measure Theory and Integration*, and the comparison of the modes of convergence to *Modes of Convergence*, both written. The **Haar measure** of an action group and the criterion of **amenability** are Part II's, in *Locally Compact Groups and Haar Measure* and *Amenable Groups*; this article uses both and does not construct them.
- The **harmonic analysis** used for the spectral criterion is the first six articles of the category, and in particular the decomposition of a unitary representation and the Fourier transform on an abelian group; the **homogeneous** and arithmetic side — lattices, arithmetic groups, homogeneous spaces — is Part II's, and the dynamics on a specific homogeneous space belongs to another article. No physics is invoked.

Throughout, $(X, \mathcal{B}, \mu)$ is a probability space — a measure space with $\mu(X) = 1$ — and measurable sets and functions are meant modulo null sets. A measurable map $T : X \to X$ is **measure-preserving** if $\mu(T^{-1}A) = \mu(A)$ for all $A \in \mathcal{B}$, and an action of a locally compact second countable group $G$ is a measurable map $G \times X \to X$, $(g, x) \mapsto gx$, with $ex = x$ and $(gh)x = g(hx)$, such that each $x \mapsto gx$ is measure-preserving. The identity of $G$ is $e$, $dx$ is a left Haar measure, and a statement holds **a.e.** (almost everywhere) if it fails on a set of measure zero; the probabilistic synonym *almost surely* is not used. The Koopman representation is written $U$, the invariant $\sigma$-algebra $\mathcal{I}$, and a Følner sequence $\{F_n\}$ as in *Amenable Groups*.

## Measure-Preserving Actions

### The Basic Definitions

**Definition.** A **measure-preserving action** of $G$ on $(X,\mathcal{B},\mu)$ is a jointly measurable map $G \times X \to X$ with $ex = x$ and $(gh)x = g(hx)$ for all $g,h \in G$ and all $x$, each transformation $x \mapsto gx$ being measure-preserving.

When $G = \mathbb{Z}$ the action is determined by the single measure-preserving transformation $T = T_1$, with $T_n = T^n$; when $G = \mathbb{Z}^d$ it is determined by $d$ commuting measure-preserving transformations; when $G = \mathbb{R}$ it is a one-parameter group $T_t$ of measure-preserving transformations, a **flow**; and for a Lie group $G$ an action by translations on a homogeneous space is the standard supply of examples.

**Definition.** A set $A \in \mathcal{B}$ is **invariant** under the action if $\mu(gA \triangle A) = 0$ for every $g \in G$; a measurable function $f$ is invariant if $f(gx) = f(x)$ a.e. for every $g$. The action is **ergodic** if every invariant set has measure $0$ or $1$.

Because the family of invariant sets is a $\sigma$-algebra modulo null sets, the definition can be phrased in terms of functions: the action is ergodic precisely when every invariant measurable function is constant a.e., and then the space decomposes as a disjoint union of orbits in the measure-theoretic sense, with no invariant proper piece.

**Proposition (the ergodic dichotomy).** The action is ergodic if and only if for every $A, B \in \mathcal{B}$ of positive measure there is $g \in G$ with $\mu(gA \cap B) > 0$.

**Proof.** If an invariant set $A$ has $0 < \mu(A) < 1$, take $B = X \setminus A$; then $gA = A$ up to null sets for every $g$, so $\mu(gA \cap B) = 0$. Conversely, if $\mu(gA \cap B) = 0$ for all $g$ and $A$ is invariant with positive measure, then $B = X \setminus A$ has $\mu(gA \cap B) = \mu(A \cap (X\setminus A)) = 0$, so $\mu(B) = 0$. $\square$

The dichotomy says that an ergodic action cannot be split, and it is the reason ergodic theory is the right frame for statistical statements: only the trivial invariant events have probability in $(0,1)$, so every invariant random variable is deterministic.

### The Koopman Representation

**Definition.** The **Koopman representation** of an action is the unitary representation $U$ of $G$ on $L^2(X,\mu)$ given by

$$
(U_g f)(x) = f(g^{-1}x).
$$

The representation is unitary because each transformation is measure-preserving, and it is strongly continuous for a second countable locally compact group acting measurably; it is a unitary representation in the sense of *Representation Theory of Locally Compact Groups*.

**Theorem (spectral form of ergodicity).** The action is ergodic if and only if the constants are the only $G$-invariant vectors of the Koopman representation: the fixed subspace is

$$
L^2(X,\mu)^G = \{\text{constant functions}\} \cong \mathbb{C}.
$$

*Proof.* An invariant function $f \in L^2$ is measurable, and its level sets $\{f > c\}$ are invariant measurable sets. If the action is ergodic each such set has measure $0$ or $1$, so $f$ is constant a.e.; conversely a non-constant invariant vector produces an invariant set of intermediate measure by taking a level set. $\square$

Thus ergodicity is a statement about a unitary representation, and the whole of the representation theory of Part II and the harmonic analysis of the first articles of this category becomes available. For $G = \mathbb{Z}$, for example, the Koopman operator $U_T$ is unitary, and the spectral theorem of standard functional analysis writes $U_T = \int_{S^1} z \, dE(z)$; the action is ergodic precisely when $E(\{1\})$ is the projection onto the constants, and it is mixing precisely when the spectral measure of every mean-zero vector is continuous at $1$.

## Mixing and Its Variants

### Strong Mixing

**Definition.** The action is **mixing** if for all $A, B \in \mathcal{B}$,

$$
\mu(gA \cap B) \longrightarrow \mu(A)\mu(B) \qquad \text{as } g \to \infty,
$$

the limit being taken in the sense that for every $\varepsilon > 0$ there is a compact $K \subseteq G$ with $|\mu(gA \cap B) - \mu(A)\mu(B)| < \varepsilon$ for every $g \notin K$.

Mixing is strictly stronger than ergodicity: it says that the sets $gA$ and $B$ become asymptotically independent, and it is the group-action form of the decay of correlations.

**Theorem (mixing criterion).** The action is mixing if and only if for all $f, h \in L^2(X,\mu)$ with $\int f \, d\mu = 0$,

$$
\langle U_g f, h \rangle \longrightarrow 0 \qquad \text{as } g \to \infty.
$$

*Proof.* The indicators of measurable sets span a dense subspace of $L^2$, and both conditions are bilinear and continuous in $(f,h)$; on indicators the first condition is the second. $\square$

**Corollary.** If the Koopman representation contains no nonzero finite-dimensional subrepresentation other than the constants, then the action is ergodic; and if in addition every matrix coefficient of the representation on the mean-zero part vanishes at infinity, then the action is mixing.

### Weak Mixing

Ergodicity is compatible with the presence of a discrete spectrum, so the decay of a single matrix coefficient is too strong a dem. The weaker notion averages over the group.

**Definition.** The action is **weakly mixing** if there is no non-constant measurable function whose orbit under the Koopman representation spans a finite-dimensional subspace; equivalently, if the representation on the mean-zero part has no finite-dimensional subrepresentation.

**Proposition.** The action is weakly mixing if and only if the product action on $(X \times X, \mu \otimes \mu)$ is ergodic.

**Proof.** The product action is ergodic precisely when the only $L^2(\mu \otimes \mu)$-invariant functions are constant; expanding an invariant function in a basis of $L^2(\mu)$ shows that this holds exactly when $L^2_0(X,\mu)$ has no finite-dimensional invariant subspace, since a finite-dimensional invariant subspace supplies a finite-rank invariant integral kernel. $\square$

For a single ergodic measure-preserving transformation $T$, the classical criterion of Koopman and von Neumann is that weak mixing is equivalent to the Cesàro convergence

$$
\frac{1}{n}\sum_{k=0}^{n-1} \bigl|\mu(T^{-k}A \cap B) - \mu(A)\mu(B)\bigr| \longrightarrow 0
$$

for all $A, B$; the average is the group-theoretic replacement of the limit along $g \to \infty$, and for an amenable group the average is taken over a Følner sequence. In the hierarchy, mixing implies weak mixing, which implies ergodicity, and neither implication reverses: a rotation of the circle is ergodic but not weakly mixing, and there are weakly mixing transformations that are not mixing.

### Mixing of Higher Order

**Definition.** The action is **mixing of order $k$** if for all $A_0, \dots, A_k \in \mathcal{B}$,

$$
\mu(g_1 A_0 \cap \cdots \cap g_k A_k) \longrightarrow \mu(A_0)\cdots\mu(A_k)
$$

as each $g_i \to \infty$ in such a way that the products $g_i g_j^{-1} \to \infty$ for $i \neq j$. An action that is mixing of every order is **mixing of all orders**.

For $\mathbb{Z}$-actions, mixing of order $2$ is mixing, and mixing of all orders is a genuinely stronger property, established for Bernoulli shifts by Kolmogorov and for many algebraic actions by Ledrappier. For a $\mathbb{Z}$-action generated by a single transformation, mixing of all orders is equivalent to the Kolmogorov property in the presence of a finite generator; for general group actions the multiple mixing problem is delicate and remains open for some standard examples.

## The Mean Ergodic Theorem

### The von Neumann Theorem for $\mathbb{Z}$

**Theorem (von Neumann).** Let $T$ be a measure-preserving transformation of $(X,\mathcal{B},\mu)$ and let $P$ be the orthogonal projection of $L^2(X,\mu)$ onto the invariant vectors. Then for every $f \in L^2(X,\mu)$,

$$
\frac{1}{n}\sum_{k=0}^{n-1} U_T^k f \longrightarrow P f \qquad \text{in } L^2(X,\mu).
$$

*Proof.* Since $U_T$ is unitary and $P$ is the projection onto $\ker(U_T - I)$, the space $L^2$ decomposes as $\ker(U_T - I) \oplus \overline{(U_T - I)L^2}$. On the kernel the average is $f = Pf$; on the image, $(U_T - I)h$ has average $n^{-1}(U_T^n h - h)$, whose norm is at most $2\|h\|/n \to 0$. Density extends the statement to the closure. $\square$

When the action is ergodic, $Pf = \int f \, d\mu \cdot \mathbf{1}$, so the theorem is the statement that the time averages converge to the space average in $L^2$. The proof uses only the unitary spectral decomposition and is therefore the model for every averaging theorem.

### Følner Sequences and Amenable Groups

For a group larger than $\mathbb{Z}$ there is no distinguished sequence of averaging sets, and one is supplied by amenability. Recall from *Amenable Groups* that a countable group $G$ is **amenable** if there is a sequence of finite nonempty sets $F_n \subseteq G$ with

$$
\frac{|gF_n \triangle F_n|}{|F_n|} \longrightarrow 0 \qquad \text{for every } g \in G,
$$

a **Følner sequence**; the definition extends to a locally compact group by replacing cardinality with Haar measure, $|F| = \mu_G(F)$, and the sequence may be taken increasing and exhausting $G$. Abelian, nilpotent and solvable groups are amenable, as are all compact groups and all finite groups; the free group $F_2$ is not, and neither is a connected semisimple Lie group with no compact factors.

**Theorem (mean ergodic theorem for amenable groups).** Let $G$ be an amenable locally compact group acting on $(X,\mathcal{B},\mu)$ by measure-preserving transformations, let $\{F_n\}$ be a Følner sequence, and let $P$ be the projection onto the invariant vectors of the Koopman representation. Then for every $f \in L^2(X,\mu)$,

$$
\frac{1}{\mu_G(F_n)}\int_{F_n} U_g f \, dg \longrightarrow P f \qquad \text{in } L^2(X,\mu).
$$

*Proof.* The operator $A_n f = \mu_G(F_n)^{-1}\int_{F_n} U_g f \, dg$ is a contraction of $L^2$ and commutes with the action, since $U_h A_n U_h^{-1}$ is the average over $hF_n$ and Følner convergence gives $\|A_n - U_h A_n U_h^{-1}\| \to 0$ for each $h$. On invariant vectors $A_n f = f$; on the closed span of $\{U_g f - f\}$ the average tends to $0$ by the Følner condition. The two pieces exhaust $L^2$ as in the abelian case, and a uniform bound plus density completes the argument. $\square$

**Corollary (equidistribution of Følner averages).** If the action is ergodic, then for every $f \in L^1(X,\mu)$ the averages $\mu_G(F_n)^{-1}\int_{F_n} U_g f \, dg$ converge to $\int f \, d\mu$ in $L^1$; for a $\mathbb{Z}$-action with $F_n = \{0, 1, \dots, n-1\}$ this is the von Neumann theorem in $L^1$.

The passage from $L^2$ to $L^1$ uses that $L^2$ is dense in $L^1$ for a probability measure; this is the reason the mean ergodic theorem is easiest in the $L^2$ setting.

### The Pointwise Theorem

**Theorem (pointwise ergodic theorem for amenable groups; Lindenstrauss).** Let $G$ be an amenable locally compact group acting on $(X,\mathcal{B},\mu)$ and let $\{F_n\}$ be a tempered Følner sequence. Then for every $f \in L^1(X,\mu)$ the averages

$$
\frac{1}{\mu_G(F_n)}\int_{F_n} f(gx) \, dg
$$

converge a.e. to the conditional expectation $\mathbb{E}[f \mid \mathcal{I}]$ of $f$ with respect to the invariant $\sigma$-algebra $\mathcal{I}$. In particular, for an ergodic action the limit is the constant $\int f \, d\mu$.

The theorem is stated here as the group-action form of the pointwise result; for $G = \mathbb{Z}$ it is Birkhoff's theorem, whose proof by the maximal inequality and the upcrossing argument is in the cited literature. The Følner form requires the Følner sequence to be **tempered**, a mild growth condition $\mu_G(F_1 \cdots F_n) \leq C \mu_G(F_n)$ that every amenable group admits, and it is for such sequences that the maximal inequality holds. For groups with a word metric one may use balls in place of Følner sets when the group has subexponential growth, but not in general.

## Ergodicity Criteria for Group Actions

### The Mautner Phenomenon

The first criterion is a contraction property of the group, and it explains why the geodesic flow is ergodic once the horocycle flow is: a function of the diagonal direction is forced to be constant along the contracted unipotent direction.

**Theorem (Mautner phenomenon).** Let $a_s$ and $u_t$ be one-parameter groups of measure-preserving transformations of $(X,\mathcal{B},\mu)$ satisfying the commutation relation

$$
a_s u_t a_s^{-1} = u_{e^{\lambda s} t}, \qquad \lambda > 0,
$$

so that the conjugates $a_s u_t a_s^{-1}$ shrink to the identity as $s \to -\infty$. Then every measurable function invariant under the $a_s$ is invariant under every $u_t$.

*Proof.* Let $f \in L^2(X,\mu)$ satisfy $f \circ a_s = f$ a.e. for every $s$, and fix $t$. For each $s > 0$ the relation gives $u_t = a_s u_{e^{-\lambda s} t} a_s^{-1}$, so

$$
f \circ u_t = f \circ a_s \circ u_{e^{-\lambda s} t} \circ a_s^{-1} = (f \circ u_{e^{-\lambda s}t}) \circ a_s^{-1},
$$

using the invariance of $f$ under $a_s$ on the left. Since each $a_s^{-1}$ preserves $\mu$,

$$
\|f \circ u_t - f\|_2^2 = \bigl\|(f \circ u_{e^{-\lambda s}t} - f) \circ a_s^{-1}\bigr\|_2^2 = \|f \circ u_{e^{-\lambda s} t} - f\|_2^2.
$$

As $s \to +\infty$ one has $e^{-\lambda s}t \to 0$, and the map $t \mapsto f \circ u_t$ is strongly continuous at $t = 0$ because a measurable measure-preserving flow acts strongly continuously on $L^2$; hence the right-hand side tends to $0$. Therefore $f \circ u_t = f$ a.e. for every $t$. $\square$

**Corollary.** If the unipotent flow $u_t$ acts ergodically on $(X,\mu)$ and $a_s$ contracts $u_t$ as in the theorem, then the flow $a_s$ acts ergodically too: an invariant function of the diagonal flow is invariant under the unipotent flow, hence constant.

This is the mechanism by which the ergodicity of the horocycle flow propagates to the geodesic flow on $G/\Gamma$ with $G = SL_2(\mathbb{R})$; the same contraction argument, with the roles of $U^+$ and $U^-$ interchanged, supplies invariance under the opposite horospherical subgroup, and the two together force invariance under the ambient group.

### Moore's Ergodicity Theorem

Let $G$ be a locally compact group and $\Gamma$ a lattice in $G$, so that $G/\Gamma$ carries a finite $G$-invariant measure. For a product group $G = G_1 \times \cdots \times G_k$ one says that $\Gamma$ is **irreducible** if its projection to each factor $G_i$ is dense.

**Theorem (Moore).** Let $G = G_1 \times \cdots \times G_k$ be a product of non-compact locally compact groups and let $\Gamma$ be an irreducible lattice in $G$. Then each factor $G_i$ acts ergodically on $G/\Gamma$.

For a semisimple Lie group with no compact factors and an irreducible lattice this is the statement that every simple factor acts ergodically on the lattice quotient, and it is the engine of homogeneous dynamics: it converts the representation theory of $G$ into ergodicity of the flows generated by its subgroups. The proof is representation-theoretic; for the factor $G_i$ it reduces to the fact that a $G_i$-invariant function that is not constant would produce a nonzero vector in a tensor product representation fixed by the other factors, and the irreducibility of the lattice forbids this.

### The Howe–Moore Theorem

Ergodicity is strengthened to mixing by a quantitative decay of matrix coefficients.

**Theorem (Howe–Moore).** Let $G$ be a connected semisimple Lie group with finite centre and no compact factors, and let $\pi$ be a unitary representation of $G$ with no nonzero $G$-invariant vector. Then every matrix coefficient $c_{v,w}(g) = \langle \pi(g)v, w\rangle$ vanishes at infinity: for every $\varepsilon > 0$ there is a compact $K \subseteq G$ with $|c_{v,w}(g)| < \varepsilon$ for $g \notin K$.

**Corollary (mixing of homogeneous actions).** If the action of $G$ on $G/\Gamma$ is ergodic, then it is mixing.

*Proof.* The Koopman representation on the mean-zero part has no invariant vectors by ergodicity, so Howe–Moore applies and the mixing criterion of the first section is satisfied. $\square$

In particular the geodesic flow on a compact hyperbolic surface is mixing, and so is the $G$-action on $G/\Gamma$ for an irreducible lattice in a higher-rank semisimple group. The decay also yields the equidistribution of translates $g\Gamma$ as $g \to \infty$ and is the analytic input to the mixing of unipotent flows on quotients of semisimple groups.

## Orbit Equivalence

### The Ratio Ergodic Theorem

For a non-singular action — one in which the transformations preserve only the measure class — the natural statement is a ratio of averages, and it holds for every ergodic action without any group-theoretic hypothesis.

**Theorem (Hopf's ratio ergodic theorem).** Let $T$ be a measure-preserving ergodic transformation of a $\sigma$-finite measure space and let $f, h \in L^1$ with $h > 0$. Then

$$
\frac{\sum_{k=0}^{n-1} f(T^k x)}{\sum_{k=0}^{n-1} h(T^k x)} \longrightarrow \frac{\int f \, d\mu}{\int h \, d\mu} \qquad \text{a.e.}
$$

The ratio theorem is the statement that the two averages have the same asymptotic normalisation, and it is the form in which the ergodic theorem survives the loss of a finite invariant measure. For a group action one replaces the sums by Følner averages; the ratio form is then the statement that the asymptotic density of an orbit in a set is proportional to the measure of the set.

### Orbit Equivalence and Dye's Theorem

**Definition.** Two measure-preserving actions of countable groups $G$ and $H$ on standard probability spaces $(X,\mu)$ and $(Y,\nu)$ are **orbit-equivalent** if there is a measure-preserving isomorphism $\phi : X \to Y$ modulo null sets carrying the $G$-orbits onto the $H$-orbits: $\phi(Gx) = H\phi(x)$ for a.e. $x$.

Orbit equivalence forgets the group and retains only the equivalence relation of lying in a common orbit; it is the coarsest equivalence relation between actions that preserves the measure-theoretic dynamics, and it is the reason amenable groups are interchangeable from the measure-theoretic point of view.

**Theorem (Dye).** Any two ergodic measure-preserving actions of amenable countable groups on a standard non-atomic probability space are orbit-equivalent.

Thus the $\mathbb{Z}$-action generated by a Bernoulli shift and the $\mathbb{Z}^2$-action generated by a pair of commuting rotations are orbit-equivalent, even though the groups differ and the actions have quite different mixing properties; orbit equivalence is blind to the group. For non-amenable groups the situation is opposite: amenability of the orbit equivalence relation is an invariant of the relation, by the theorem of Connes, Feldman and Weiss, so no ergodic action of a non-amenable group is orbit-equivalent to an action of an amenable group. The von Neumann algebra of the equivalence relation is the finer invariant that distinguishes the remaining cases.

**Theorem (Kac's lemma).** Let $T$ be an ergodic measure-preserving transformation of a probability space and let $A$ have $\mu(A) > 0$. Then the expected first return time to $A$ starting from a point of $A$ is $1/\mu(A)$.

*Proof.* The sets $A_k = \{x \in A : T^k x \in A \text{ and } T^j x \notin A \text{ for } 0 < j < k\}$ are disjoint and their union is $A$ up to a null set, by ergodicity and recurrence; their $T$-translates partition the complement of the union of the far past, and the invariant measure computation gives $\sum_{k \geq 1} \mu(A_k) = \mu(A)$ while $\sum_{k\geq1} k\mu(A_k) = 1$. Hence the mean return time is $1/\mu(A)$. $\square$

Kac's lemma is the quantitative form of Poincaré recurrence, and it is the seed of the return-time theory: the distribution of the rescaled return times converges under the induced map to an exponential law when the flow has a suitable mixing property, which is the basis of the orbit-equivalence constructions of Dye and Ornstein–Weiss.

## Examples

### Translations of Tori

**Example.** Let $G = \mathbb{Z}$ act on the torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ by the translation $T_a(x) = x + a$. The action is ergodic if and only if $1, a_1, \dots, a_n$ are rationally independent.

Indeed, by the harmonic analysis of *Harmonic Analysis on Groups* the characters $\chi_m(x) = e^{2\pi i \langle m, x\rangle}$ form an orthonormal basis of $L^2(T^n)$ and diagonalise the Koopman operator: $U_{T_a}\chi_m = e^{-2\pi i\langle m,a\rangle}\chi_m$. Each character is an eigenfunction, so the mean of a character over the orbit is

$$
\frac{1}{N}\sum_{k=0}^{N-1} e^{2\pi i k \langle m,a\rangle} \longrightarrow \begin{cases} 1, & \langle m, a\rangle \in \mathbb{Z}, \\ 0, & \text{otherwise}, \end{cases}
$$

by the geometric series. Hence the only characters fixed by $T_a$ other than the constant are those with $\langle m,a\rangle \in \mathbb{Z}$ for some $m \neq 0$, and ergodicity fails exactly when such an $m$ exists, that is, exactly when $1, a_1, \dots, a_n$ are rationally dependent. The same computation with a $\mathbb{Z}^d$-action generated by $a^{(1)}, \dots, a^{(d)}$ shows that the action is ergodic if and only if the only integer vector $(m_1,\dots,m_d)$ with $\langle m_i, a^{(j)}\rangle \in \mathbb{Z}$ for all $j$ is zero, i.e. if and only if the matrix with rows $a^{(j)}$ together with the row $(1,\dots,1)$ has rank $d+1$ over $\mathbb{Q}$.

A rotation is never mixing: the eigenfunction computation shows $\langle U_{T_a}\chi_m, \chi_m\rangle = e^{-2\pi i\langle m,a\rangle}$ does not tend to $0$, so the spectral measure is discrete and there is no decay of correlations. Thus ergodicity and mixing are genuinely different, and the rotation is the standard witness.

**Example (ergodic algebraic $\mathbb{Z}^2$-action).** Let $A \in SL_2(\mathbb{Z})$ have $|\operatorname{tr} A| > 2$, so that it is hyperbolic with eigenvalues $\lambda, \lambda^{-1}$ of modulus not $1$; let $\mathbb{Z}^2$ act on $T^2$ by $A^{m} A_1^{m_1}$, where $A_1$ is a second matrix chosen so that the action is generated by two commuting automorphisms. The action is ergodic, and this is the algebraic model of an Anosov system: the hyperbolic structure of $A$ supplies the unstable directions along which the orbit separates exponentially. The two-dimensional case is the elementary instance of the general fact that a $\mathbb{Z}^d$-action by automorphisms of a torus is ergodic when the eigenvalues of the generators have no common root of unity on the unit circle.

### Bernoulli and Algebraic Actions

**Example (Bernoulli shift).** Let $(\Omega, \mathbb{P})$ be a probability space and let $X = \Omega^{\mathbb{Z}}$ carry the product measure; the **Bernoulli shift** is the $\mathbb{Z}$-action generated by $\sigma(\omega)_n = \omega_{n+1}$. It is mixing of all orders: for cylinder sets $A$ and $B$ depending on coordinates in finite windows, $\mu(\sigma^{-k}A \cap B) = \mu(A)\mu(B)$ as soon as $k$ exceeds the width of the windows, so the convergence is exact, and the same argument with $k$ shifts applies to finitely many cylinder sets simultaneously. The Bernoulli shift is the model of a completely random action, and its orbit equivalence class is the class of all ergodic amenable actions by Dye's theorem.

**Example (the boundary action of $F_2$).** Let $F_2$ act on its space of infinite reduced words with the natural measure. The action is ergodic and, for the action on the boundary, it is not amenable; the orbit equivalence relation of the action on the boundary carries a von Neumann algebra of type $\mathrm{III}$, in contrast with the type $\mathrm{II}_1$ algebra of an orbit equivalence relation of an amenable action. This is the standard measure-theoretic witness that amenability of the group is visible in the dynamics.

### Homogeneous Actions and Flows

**Example (the geodesic and horocycle flows).** Let $G = SL_2(\mathbb{R})$, let $\Gamma = SL_2(\mathbb{Z})$, and let $X = G/\Gamma$ with its finite $G$-invariant measure. The **horocycle flow** is the flow of the unipotent subgroup

$$
u_t = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}, \qquad U = \left\{u_t : t \in \mathbb{R}\right\},
$$

and the **geodesic flow** is the flow of the diagonal subgroup $A = \{\operatorname{diag}(e^{t/2}, e^{-t/2})\}$. The Mautner relation $a_s u_t a_s^{-1} = u_{e^{-s}t}$ holds, so the Mautner phenomenon reduces the invariant functions of the geodesic flow to those of the horocycle flow; the horocycle flow is ergodic by a direct argument using the structure of $\Gamma$, and hence so is the geodesic flow. By Howe–Moore the geodesic flow is in fact mixing, with exponential decay of correlations. The horocycle flow, by contrast, is uniquely ergodic but not mixing: it is a distal flow, and its mixing defect measures the presence of the unipotent direction. These examples are the prototypical instances of the general theory, and the dynamics of a general $G/\Gamma$ is developed.

**Example (flows on nilmanifolds).** Let $N$ be a simply connected nilpotent Lie group with a lattice $\Gamma$, and let $\{u_t\}$ be a one-parameter subgroup. The action of $u_t$ on $N/\Gamma$ is ergodic if and only if the flow is not confined to a smaller closed orbit, and the general principle — that the orbit closure is a submanifold and the flow is uniquely ergodic on it — is the content of Ratner's topological theorem for unipotent flows. The rotation flow of the two-torus, the special case in which $N = \mathbb{R}^2$ and $\Gamma = \mathbb{Z}^2$, is the elementary instance; the Heisenberg nilmanifold is the first genuinely non-abelian case and exhibits a unipotent flow that is mixing in the direction of the centre and periodic in the transverse direction.

## Summary

An action of a locally compact group $G$ by measure-preserving transformations of a probability space $(X,\mathcal{B},\mu)$ is ergodic when every invariant set has measure $0$ or $1$, equivalently when every invariant measurable function is constant a.e., and the Koopman representation $U_g f(x) = f(g^{-1}x)$ turns this into the condition that the constants are the only invariant vectors of a unitary representation of $G$. Mixing is the decay $\mu(gA \cap B) \to \mu(A)\mu(B)$ as $g \to \infty$, equivalently the vanishing of the matrix coefficients of the Koopman representation on the mean-zero part; weak mixing replaces the limit by a Følner average and is equivalent to the ergodicity of the product action; and mixing of higher order strengthens the decay of correlations for several translates at once.

For an amenable group, a Følner sequence $\{F_n\}$ supplies the averaging sets, and the mean ergodic theorem asserts that $\mu_G(F_n)^{-1}\int_{F_n} U_g f \, dg \to Pf$ in $L^2$, with $Pf$ the projection onto the invariant vectors; the pointwise theorem of Lindenstrauss asserts convergence a.e. to the conditional expectation on the invariant $\sigma$-algebra for tempered Følner sequences. For a single transformation these are the von Neumann and Birkhoff theorems, stated here as standard with their proofs in the cited literature.

The Mautner phenomenon propagates ergodicity along the relation $a^n u a^{-n} \to e$; Moore's theorem gives the ergodicity of every non-compact closed subgroup of an irreducible lattice quotient, and the Howe–Moore theorem gives the decay at infinity of the matrix coefficients of a representation without invariant vectors, hence the mixing of an ergodic homogeneous action. Hopf's ratio ergodic theorem is the form of the ergodic theorem that survives the absence of a finite invariant measure, and orbit equivalence — with Dye's theorem that all ergodic amenable actions on a standard non-atomic space are orbit-equivalent — is the coarsest measure-theoretic equivalence of actions. The examples are the rationally independent translations of a torus, which are ergodic and never mixing; the Bernoulli shift, mixing of all orders; the hyperbolic torus automorphisms; and the horocycle and geodesic flows on $SL_2(\mathbb{Z})\backslash SL_2(\mathbb{R})$, where the Mautner relation between the unipotent and diagonal subgroups is what carries ergodicity from one to the other.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X, \mathcal{B}, \mu)$ | Probability space, $\mu(X)=1$, of an action |
| $G$, $e$, $dx$, $\mu_G$ | Locally compact second countable group, identity, left Haar measure |
| $gx$, $gA$ | Action of $g$ on a point, on a set |
| a.e. | Almost everywhere; the probabilistic synonym *almost surely* is not used |
| invariant, ergodic | $\mu(gA\triangle A)=0$ for all $g$; every invariant set has measure $0$ or $1$ |
| $\mathcal{I}$ | Invariant $\sigma$-algebra; $\mathbb{E}[f \mid \mathcal{I}]$ the invariant conditional expectation |
| $U_g$, $U_T$ | Koopman representation $U_g f(x)=f(g^{-1}x)$ |
| $P$ | Orthogonal projection onto the invariant vectors |
| mixing | $\mu(gA\cap B)\to\mu(A)\mu(B)$ as $g\to\infty$ |
| weakly mixing | product action ergodic; no finite-dimensional mean-zero invariant subspace |
| mixing of order $k$ | joint decay for $k$ translates with $g_i g_j^{-1}\to\infty$ |
| $F_n$ | Følner sequence: $\lvert gF_n\triangle F_n\rvert/\lvert F_n\rvert\to0$ |
| amenable | existence of a Følner sequence (Part II, *Amenable Groups*) |
| tempered | growth condition $\mu_G(F_1\cdots F_n)\le C\mu_G(F_n)$ on a Følner sequence |
| Mautner | $a_s u_t a_s^{-1}=u_{e^{\lambda s}t}$: $A$-invariant functions are $u_t$-invariant |
| Moore's theorem | each non-compact factor acts ergodically on the quotient by an irreducible lattice |
| Howe–Moore | matrix coefficients of an invariant-free representation vanish at infinity |
| orbit equivalence | measure isomorphism carrying orbits to orbits |
| Kac's lemma | expected return time to $A$ is $1/\mu(A)$ |
| $T_a(x)=x+a$ | Translation of the torus $T^n=\mathbb{R}^n/\mathbb{Z}^n$ |
| $u_t$, $a_s$ | Horocycle and diagonal (geodesic) one-parameter subgroups of $SL_2(\mathbb{R})$ |







## Further Reading

- Paul R. Halmos, *Lectures on Ergodic Theory* (Chelsea, 1956; reprinted AMS, 2006), for the classical von Neumann and Birkhoff theorems and the ergodicity of translations.
- I. P. Cornfeld, S. V. Fomin and Ya. G. Sinai, *Ergodic Theory* (Springer, 1982), for the general theory, mixing and the spectral classification.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the pointwise ergodic theorem, the ergodic decomposition and entropy.
- Ulrich Krengel, *Ergodic Theorems* (De Gruyter, 1985), for the mean and pointwise theorems in their most general form, including amenable groups.
- Elon Lindenstrauss, "Pointwise theorems for amenable groups", *Inventiones Mathematicae* 146 (2001), 259–295, for the pointwise ergodic theorem for tempered Følner sequences.
- Robert J. Zimmer, *Ergodic Theory and Semisimple Groups* (Birkhäuser, 1984), for Moore's theorem, the Mautner phenomenon and the ergodic theory of lattice actions.
- David Fisher, *Groups Acting on Manifolds: Rigidity and Dynamics* (Cambridge University Press, 2019), for the Howe–Moore theorem and the modern rigidity theory of group actions.
- Henry B. Mann, *Addition Theorems* (Interscience, 1965), for the Følner condition and the combinatorial form of amenability.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
