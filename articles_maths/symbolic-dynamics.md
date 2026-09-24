
# __Symbolic Dynamics__

## Introduction

**Symbolic dynamics** replaces a topological dynamical system by a set of sequences over a finite alphabet with the shift as the dynamics. The shift is the simplest non-trivial system that exists: the map that forgets the first coordinate of a bi-infinite sequence and reads the next one; it is a homeomorphism of a compact, perfect, totally disconnected space, its periodic points are the periodic sequences and hence are dense, it is mixing, its entropy is the logarithm of the alphabet size, and every continuous map commuting with it is given by a finite sliding block of coordinates. The interest of the subject is that this simple model is universal: every hyperbolic system is a factor of a subshift of finite type by the theory of Markov partitions, every continuous map of the interval with positive entropy contains a subsystem conjugate to a subshift, and every dynamical system defined by a finite set of forbidden words is a shift of finite type whose periodic orbit counts, entropy and zeta function are computed from a single matrix. Symbolic dynamics is therefore both a source of examples — the full shift, the golden-mean shift, the Sturmian and substitution subshifts, the sofic shifts — and the classification tool by which the topological dynamics of the smooth and hyperbolic systems is converted into finite combinatorics.

The article begins with the shift spaces: the full shift on a finite alphabet, its topology as a Cantor set, the cylinders, the shift and the metric; then the subshifts, their languages, their presentation by forbidden words and the fundamental identity between the topological entropy and the exponential growth of the number of words, $h=\lim_n\frac1n\log|\mathcal L_n|$. The **subshifts of finite type** follow, with the transition matrix, the computation of the entropy as the logarithm of its spectral radius, the **zeta function** $\zeta(t)=1/\det(I-tA)$ of Bowen and Lanford and the growth of the periodic points, and then the **sofic shifts**, the factors of the shifts of finite type, described by labelled graphs. The coding theory is treated next: the sliding block codes and the theorem of Curtis–Hedlund–Lyndon that every continuous shift-commuting map is one, the factor maps and the semiconjugacies, the **Markov partitions** of the hyperbolic sets of *Hyperbolic Dynamics and Anosov Systems* that realise them, and the classification of the shifts of finite type by **strong shift equivalence** and the dimension group, with the theorem of Williams and the counterexamples that separate strong shift equivalence from shift equivalence. The article closes with the entropy and the periodic orbit counts, the Sturmian and substitution subshifts with their complexity, the theorem of Morse and Hedlund, and the arithmetic codings whose dynamics belongs.

The shift spaces are studied with the topology of *Topological Spaces* and *Metric, Uniform and Complete Spaces*, the Cantor set being the model compact perfect totally disconnected space; the transitivity, the mixing, the entropy and the periodic points are those of *Topological Dynamics*; the horseshoe and its symbolic model are those of *Chaos and Strange Attractors*; the Markov partitions and the Anosov systems are those of *Hyperbolic Dynamics and Anosov Systems*; the measure-theoretic entropy and the Bernoulli measures are those of *Ergodic Theory*. The arithmetic and continued-fraction codings lie outside this article.

No physics is invoked.

## Shift Spaces

### The Full Shift

**Definition.** Let $\mathcal A=\{0,1,\dots,d-1\}$ be a finite **alphabet** of cardinality $d \ge2$. The **full shift** on $\mathcal A$ is the set

$$
\Sigma_d=\mathcal A^{\mathbb{Z}}=\{x=(x_n)_{n \in\mathbb{Z}}:x_n \in\mathcal A\}
$$

with the **shift** $\sigma:\Sigma_d\to\Sigma_d$, $(\sigma x)_n=x_{n+1}$; the one-sided full shift is $\Sigma_d^+=\mathcal A^{\mathbb{N}}$ with the same formula. The set carries the product topology of the discrete topologies, which is induced by the metric

$$
d(x,y)=2^{-\min\{|n|:x_n\neq y_n\}}
$$

(with $d(x,x)=0$), and the sets $[w]=\{x:x_m\cdots x_{m+n-1}=w\}$ indexed by the finite **words** $w \in\mathcal A^n$ and the positions $m \in\mathbb{Z}$ are the **cylinders**; they form a countable base of clopen sets.

**Theorem (the structure of the full shift).** (i) $\Sigma_d$ is compact, perfect, totally disconnected and metrisable; it is homeomorphic to the middle-third Cantor set, and every compact, perfect, totally disconnected metrisable space is homeomorphic to it.

(ii) The shift $\sigma$ is a homeomorphism of $\Sigma_d$, topologically transitive and topologically mixing; its periodic points are dense, and the fixed points of $\sigma^n$ are the sequences of period dividing $n$, of which there are $d^n$.

(iii) The topological entropy of $\sigma$ is $h_{\mathrm{top}}(\sigma)=\log d$, and the Bernoulli measure $\mu$ with weights $p_0,\dots,p_{d-1}$ is $\sigma$-invariant and ergodic, with measure-theoretic entropy $-\sum_ip_i\log p_i$; the measure of maximal entropy is the uniform Bernoulli measure.

*Proof.* The space $\Sigma_d$ is a product of compact spaces, hence compact by the Tychonoff theorem, and the metric induces the product topology; the perfectness and the total disconnectedness are immediate from the definition of the cylinders, and the Cantor–Bendixson analysis of *Topological Spaces* gives the homeomorphism with the middle-third Cantor set. The shift conjugates the cylinders, hence is a homeomorphism, and its mixing follows from the fact that for words $u,v$ and $n$ exceeding the length of $u$, the cylinder $[u]$ meets $\sigma^{-n}[v]$ in a nonempty clopen set. The density of the periodic points is the fact that every cylinder $[w]$ contains the periodic sequence $\overline{w}$ of period $|w|$, and the entropy is computed by the count $d^n$ of the words of length $n$; the Bernoulli statements are those of *Ergodic Theory*. $\square$

### Subshifts and Languages

**Definition.** A **subshift** is a closed $\sigma$-invariant subset $X \subseteq\Sigma_d$; it is **minimal** if no proper nonempty closed invariant subset exists, **transitive** and **mixing** in the senses of *Topological Dynamics*, and **irreducible** when for every pair of words $u,v \in\mathcal L(X)$ there is a word $w$ with $uwv \in\mathcal L(X)$. The **language** of $X$ is the set

$$
\mathcal L(X)=\{w \in\mathcal A^n:n \ge0,\ w \text{ occurs in some } x \in X\},
$$

with $\mathcal L_n(X)=\mathcal L(X)\cap\mathcal A^n$; a subshift is **determined** by its language, and the **forbidden words** of $X$ are the words that do not occur in it, so that $X=\{x:\text{no block of } x \text{ is forbidden}\}$.

**Theorem (entropy and the language).** Let $X$ be a subshift. Then the topological entropy of the shift restricted to $X$ is

$$
h_{\mathrm{top}}(\sigma|_X)=\lim_{n\to\infty}\frac1n\log|\mathcal L_n(X)|,
$$

the exponential growth rate of the language.

*Proof (sketch).* The language of the join of the covers by the cylinders gives exactly $|\mathcal L_n(X)|$, and the limit formula for the entropy of a subshift follows from the Morse–Hedlund theory of the complexity; the logarithm of the number of the words of length $n$ counts the orbits distinguishable at resolution $n$. $\square$

**Example (the golden-mean shift).** Let $X$ be the subshift of $\Sigma_2$ whose forbidden word is $11$, so that $X$ consists of the sequences with no two consecutive ones. Its language of length $n$ is the set of binary words with no $11$, of cardinality the Fibonacci number $F_{n+2}$; a direct count gives $|\mathcal L_n(X)|=2,3,5,8,13,21,\dots$ and

$$
h_{\mathrm{top}}(\sigma|_X)=\lim_n\frac1n\log F_{n+2}=\log\varphi, \qquad \varphi=\frac{1+\sqrt5}{2}=1.618034\ldots
$$

the logarithm of the golden ratio, in agreement with the matrix computation of the next section.

## Subshifts of Finite Type and Sofic Shifts

### Transition Matrices

**Definition.** Let $A$ be a $d\times d$ matrix with entries in $\{0,1\}$. The **subshift of finite type** (SFT) with transition matrix $A$ is

$$
\Sigma_A=\{x \in\Sigma_d:A_{x_nx_{n+1}}=1 \text{ for all } n \in\mathbb{Z}\},
$$

equivalently the subshift whose forbidden words are the pairs $ij$ with $A_{ij}=0$. A subshift is of finite type if it is of this form up to topological conjugacy; it is $k$-step if the forbidden words have length at most $k$, and the **edge shift** of a directed graph $G$ has the edges of $G$ as its alphabet and the paths of $G$ as its sequences, which is an SFT with the adjacency matrix of $G$.

**Theorem (entropy and zeta function of an SFT).** Let $X=\Sigma_A$ be an SFT with irreducible transition matrix $A$. Then

(i) $h_{\mathrm{top}}(\sigma|_X)=\log\rho(A)$, where $\rho(A)$ is the spectral radius, and the entropy is realised by the measure corresponding to the Perron eigenvector of $A$;

(ii) the number of fixed points of $\sigma^n$ satisfies $p_n=\operatorname{tr}(A^n)$, and the **zeta function** of the subshift,

$$
\zeta_X(t)=\exp\Bigl(\sum_{n\ge1}\frac{p_n}{n}t^n\Bigr)=\frac1{\det(I-tA)},
$$

is rational, the identity being the formula of Bowen and Lanford;

(iii) the entropy is positive exactly when $\rho(A)>1$; for a primitive $A$ the growth of the periodic points is $p_n=\operatorname{tr}(A^n)\sim\rho(A)^n$, while for an irreducible matrix that is periodic of period $m$ the maximal eigenvalues are $m$ distinct numbers of modulus $\rho(A)$ and $p_n$ carries a periodic factor, so that no single exponential asymptotic holds.

*Proof.* The number of words of length $n$ of $X$ is the sum of the entries of $A^{n-1}$, so its growth rate is $\rho(A)$ by the Perron–Frobenius theorem, and (i) follows from the language formula for the entropy. The fixed points of $\sigma^n$ correspond to the closed paths of length $n$ in the graph of $A$, counted by $\operatorname{tr}(A^n)$, which gives (ii) after expanding the logarithm of the determinant as $\sum_n\frac{\operatorname{tr}(A^n)}{n}t^n$. The asymptotic in (iii) is the Perron–Frobenius asymptotics, which requires primitivity for a single exponential and otherwise gives the periodic factor described there. $\square$

**Example (the full shift and the golden-mean shift).** For the full $d$-shift the matrix is the $d\times d$ all-ones matrix, $\operatorname{tr}(A^n)=d^n$, and $\det(I-tA)=1-dt$, so $\zeta(t)=1/(1-dt)$ and the entropy is $\log d$. For the golden-mean shift the matrix is

$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}, \qquad \det(I-tA)=1-t-t^2,
$$

so $\zeta(t)=1/(1-t-t^2)$, the fixed points of $\sigma^n$ number $\operatorname{tr}(A^n)=1,3,4,7,11,18,29,\dots$, the Lucas numbers, and the spectral radius is the golden ratio, since the characteristic polynomial is $\lambda^2-\lambda-1$; the entropy is $\log\varphi$ computed above.

### Sofic Shifts

**Definition.** A **sofic shift** is a subshift that is the image of an SFT under a continuous shift-commuting surjection, equivalently the set of the bi-infinite sequences of labels of the paths of a finite directed labelled graph; the graph is a **presentation** of the shift, and the right-resolving presentations — those in which at most one edge leaves each vertex with a given label — are the computational ones.

**Theorem (presentations and entropy).** Every sofic shift has a right-resolving presentation, and from a right-resolving presentation the entropy is computed as the logarithm of the spectral radius of the underlying adjacency matrix; sofic shifts are closed under the operations of factoring, and the class of the sofic shifts is strictly larger than that of the shifts of finite type. For an irreducible sofic shift the **Fischer cover**, the minimal right-resolving presentation, is unique up to isomorphism, and it is the computational tool for the entropy and the periodic orbit counts of the shift.

## Sliding Block Codes and Coding

### Sliding Block Codes

**Definition.** Let $X \subseteq\Sigma_{\mathcal A}$ and $Y \subseteq\Sigma_{\mathcal B}$ be subshifts. A **sliding block code** with memory $m$ and anticipation $a$ is a map $\phi:X\to Y$ given by a function $\Phi:\mathcal A^{m+a+1}\to\mathcal B$ such that

$$
\phi(x)_n=\Phi(x_{n-m}\cdots x_{n+a}) \qquad \text{for all } n ,
$$

and a **block code** is the one-sided analogue. A **conjugacy** is a bijective sliding block code whose inverse is again a sliding block code, and a **factor map** is a surjective one.

**Theorem (Curtis–Hedlund–Lyndon).** A map $\phi:X\to Y$ between subshifts is continuous and commutes with the shifts, $\phi\circ\sigma=\sigma\circ\phi$, if and only if it is a sliding block code.

*Proof.* If $\phi$ is a sliding block code, the continuity is clear because the $n$-th coordinate of the image depends only on finitely many coordinates of the input, and the commutation with the shift is the translation invariance of the block rule. Conversely, if $\phi$ is continuous and commutes with the shift, the compactness of $X$ gives a finite cylinder $[w]$ whose image lies in the cylinder $[\phi(x)_0]$ of the zeroth coordinate, and the commutation extends the rule to all the coordinates, producing the sliding block. $\square$

### Markov Partitions and the Coding of Hyperbolic Systems

**Theorem (coding of a hyperbolic set).** Let $\Lambda$ be a locally maximal hyperbolic set for a diffeomorphism $f$ with $f|_\Lambda$ topologically transitive, and let $\mathcal R$ be a Markov partition of $\Lambda$ with transition matrix $A$, as in *Hyperbolic Dynamics and Anosov Systems*. Then there is a continuous surjection $\pi:\Sigma_A\to\Lambda$ with $\pi\circ\sigma=f\circ\pi$ which is a sliding block code and is finite-to-one, one-to-one on a residual set, and injective on the periodic points; consequently $\Lambda$ is a factor of the SFT $\Sigma_A$, the topological entropy is $h_{\mathrm{top}}(f|_\Lambda)=\log\rho(A)$, and the periodic orbits of $f$ in $\Lambda$ are counted by $\operatorname{tr}(A^n)$. The coding is the bridge between the analysis of the hyperbolic system and the finite combinatorics of the transition matrix, and the horseshoe of *Chaos and Strange Attractors* is the special case in which $\pi$ is already a conjugacy onto the full two-shift.

### Classification of the Shifts of Finite Type

**Definition.** Two square matrices $A,B$ with entries in $\mathbb{N}$ are **elementary strong shift equivalent** if there are rectangular matrices $R,S$ with $A=RS$ and $B=SR$ over $\mathbb{N}$, and **strong shift equivalent** if they are related by a finite chain of elementary equivalences; they are **shift equivalent** if there are matrices $R,S$ and an integer $\ell$ with $A^\ell=RS$, $B^\ell=SR$, $AR=RB$ and $SA=BS$. The **dimension group** of an SFT is the pair $(\mathbb{Z}^d,S)$ with $S=A$ acting on the inductive limit of the $\mathbb{Z}^d$ along $A$, and it is an invariant of conjugacy.

**Theorem (Williams; Bowen–Franks).** Let $A$ and $B$ be the transition matrices of SFTs. If $A$ and $B$ are strong shift equivalent then the shifts $\Sigma_A$ and $\Sigma_B$ are topologically conjugate, and if the shifts are conjugate then $A$ and $B$ are shift equivalent; shift equivalence is decided by the dimension group, which is a complete invariant of shift equivalence. The implication from shift equivalence to conjugacy — the **shift equivalence conjecture** of Williams — fails in general: Kim and Roush produced shift equivalent reducible matrices whose shifts are not conjugate, and the irreducible case is an open problem. The correct classification requires the finer relation of strong shift equivalence, which has no known decision procedure in general.

## Complexity, Substitutions and Examples

### Complexity and the Theorem of Morse and Hedlund

**Definition.** The **complexity** of a subshift $X$ is the function $n\mapsto p_X(n)=|\mathcal L_n(X)|$. The theorem of Morse and Hedlund states that if a one-sided infinite word satisfies $p(n)\le n$ for some $n \ge1$, then the word is eventually periodic; a word with $p(n)=n+1$ for all $n$ is a **Sturmian** word, and its subshift is minimal, has zero entropy, and is uniquely ergodic.

**Example (Sturmian and rotation codings).** For an irrational $\alpha \in(0,1)$ and the rotation $R_\alpha$ of the circle, the coding of the orbit of a point with respect to the partition of the circle into the two intervals of lengths $\alpha$ and $1-\alpha$ is a Sturmian word over two symbols; the associated subshift is minimal, has complexity $p(n)=n+1$ and zero entropy, and it is not of finite type. The Sturmian subshift is the symbolic model of the irrational rotation: the rotation is a continuous at most two-to-one factor of the subshift, so the subshift is minimal and zero-entropy but is not equicontinuous, and its arithmetic — the continued fraction of $\alpha$ and the recurrence of the return times — belongs.

**Example (substitution subshifts).** A **substitution** is a map $\tau:\mathcal A\to\mathcal A^+$ extended to words and to sequences; the subshift generated by the fixed point of a primitive substitution is minimal and uniquely ergodic, and its complexity and entropy are computed from the incidence matrix of $\tau$, whose Perron eigenvalue gives the entropy. For the **Fibonacci substitution** $0\mapsto01$, $1\mapsto0$ the subshift is the Sturmian subshift of slope $\varphi-1$ with complexity $n+1$ and zero entropy; for the **Thue–Morse** substitution the subshift is minimal, uniquely ergodic, of zero entropy, and of linear complexity, its complexity growing like a constant times $n$ rather than like $n+1$.

### The $\beta$-Shift and Other Codings

**Example (the $\beta$-shift).** For a real $\beta>1$ the **$\beta$-shift** is the subshift of $\{0,\dots,\lceil\beta\rceil-1\}^{\mathbb N}$ whose sequences are the $\beta$-expansions of the numbers in $[0,1)$; its entropy is $\log\beta$, and it is sofic when the $\beta$-expansion of $1$ is eventually periodic, in particular when $\beta$ is a Pisot number; conversely the soficity forces $\beta$ to be a **Perron number** — an algebraic integer all of whose conjugates are smaller in modulus — by the theorem of Bertrand. For $\beta=\varphi$ the $\beta$-shift is the golden-mean shift of the previous section, so that the arithmetic of the expansion and the combinatorics of the forbidden word $11$ are the same object.

**Example (the horseshoe and the solenoid in symbolic form).** The invariant set of the Smale horseshoe is conjugate to the full two-shift; the solenoid of *Chaos and Strange Attractors* is the inverse limit of the doubling map and its symbolic model is the one-sided two-shift, and the Anosov diffeomorphisms of the torus are coded by the Markov partitions built from their stable and unstable foliations, so that their periodic orbit counts are computed by the transition matrices, as in *Hyperbolic Dynamics and Anosov Systems*.

## Summary

The **full shift** $\sigma$ on $\Sigma_d=\mathcal A^{\mathbb Z}$ is a homeomorphism of a compact perfect totally disconnected space, homeomorphic to the middle-third Cantor set; it is mixing, its periodic points are dense, the fixed points of $\sigma^n$ number $d^n$, and $h_{\mathrm{top}}(\sigma)=\log d$, with the Bernoulli measures as the invariant measures. A **subshift** is a closed invariant subset, determined by its **language** $\mathcal L(X)$ or by its forbidden words, and its entropy is the exponential growth rate of the language, $h_{\mathrm{top}}(\sigma|_X)=\lim_n\frac1n\log|\mathcal L_n(X)|$. A **subshift of finite type** $\Sigma_A$ is defined by a $\{0,1\}$-matrix $A$; its entropy is $h_{\mathrm{top}}=\log\rho(A)$ by Perron–Frobenius, the fixed points of $\sigma^n$ number $\operatorname{tr}(A^n)$, and the Bowen–Lanford **zeta function** is $\zeta_X(t)=\exp\sum_n\frac{p_n}{n}t^n=1/\det(I-tA)$, rational; the full $d$-shift has $\zeta=1/(1-dt)$ and the golden-mean shift has matrix $\begin{pmatrix}1&1\\1&0\end{pmatrix}$, $\zeta=1/(1-t-t^2)$, $p_n$ the Lucas numbers and entropy $\log\varphi$. A **sofic shift** is the image of an SFT, or the set of labels of the paths of a finite labelled graph, and its entropy is read from a right-resolving presentation.

A **sliding block code** is a shift-commuting map given by a finite block rule, and the theorem of Curtis–Hedlund–Lyndon states that these are exactly the continuous shift-commuting maps; a **Markov partition** of a locally maximal hyperbolic set produces a sliding block code from an SFT onto the set which is finite-to-one and injective on the periodic points, giving $h_{\mathrm{top}}=\log\rho(A)$ and the periodic orbit counts. The classification of the shifts of finite type is by **strong shift equivalence**, with **shift equivalence** and the **dimension group** as a decidable invariant; conjugacy implies shift equivalence by Williams and Bowen–Franks, and the converse fails in general, so the shift equivalence conjecture is false. The **complexity** $p(n)$ of a subshift satisfies the Morse–Hedlund theorem — $p(n)\le n$ forces eventual periodicity — and the **Sturmian** words with $p(n)=n+1$ are the minimal zero-entropy codings of irrational rotations; the **substitution** subshifts, the $\beta$-shifts and the **horseshoe** and solenoid models are the standard examples, the arithmetic of the codings belonging.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal A$, $d$ | alphabet and its cardinality |
| $\Sigma_d=\mathcal A^{\mathbb Z}$, $\Sigma_d^+$ | full two-sided and one-sided shift |
| $\sigma$ | shift map |
| $[w]$ | cylinder of the word $w$ |
| $\mathcal L(X)$, $\mathcal L_n(X)$ | language and words of length $n$ |
| $X$, $\Sigma_A$ | subshift and subshift of finite type |
| $A$ | transition (adjacency) matrix |
| $\rho(A)$, $\varphi$ | spectral radius, golden ratio |
| $p_n$, $\zeta_X$ | periodic points of period $n$, zeta function |
| $\pi$ | coding map of a Markov partition |
| $p_X(n)$ | complexity of a subshift |
| $\tau$ | substitution |
| $\beta$ | parameter of the $\beta$-shift |





## Further Reading

- Rufus Bowen and Oscar E. Lanford III, "Zeta functions of restrictions of the shift transformation", in *Global Analysis* (American Mathematical Society, 1970), 43–49, for the rationality of the zeta function of a shift of finite type.
- Roy L. Adler, "Symbolic dynamics and Markov partitions", *Bulletin of the American Mathematical Society* 35 (1998), 1–56, for a survey of the coding of the hyperbolic systems by the shifts of finite type.
- Robert F. Williams, "Classification of subshifts of finite type", *Annals of Mathematics* 98 (1973), 120–153, and "Classification of subshifts of finite type: errata", *Annals of Mathematics* 99 (1974), 380–381, for the strong shift equivalence classification and the conjecture relating it to shift equivalence.
- Ki Hang Kim and Fred W. Roush, "The Williams conjecture is false for reducible subshifts", *Journal of the American Mathematical Society* 12 (1999), 573–581, for the counterexamples that separate shift equivalence from conjugacy.
- Mike Boyle, Brian Marcus and Paul Trow, "Resolving maps and the dimension group for shifts of finite type", *Memoirs of the American Mathematical Society* 377 (1987), for the dimension group and its role in the classification.
- Douglas Lind and Brian Marcus, *An Introduction to Symbolic Dynamics and Coding* (Cambridge University Press, 1995), for the systematic theory of the subshifts, sofic shifts, sliding block codes and entropy.
- Marston Morse and Gustav A. Hedlund, "Symbolic dynamics", *American Journal of Mathematics* 60 (1938), 815–866, and "Symbolic dynamics II: Sturmian trajectories", *American Journal of Mathematics* 62 (1940), 1–42, for the complexity, the Morse–Hedlund theorem and the Sturmian words.
- Martine Queffélec, *Substitution Dynamical Systems — Spectral Analysis* (Springer, 1987), and N. Pytheas Fogg, *Substitutions in Dynamics, Arithmetics and Combinatorics* (Springer, 2002), for the substitution subshifts, their complexity and their ergodic theory.
- Anne Bertrand, "Développements en base de Pisot et répartition modulo 1", *Comptes Rendus de l'Académie des Sciences* 285 (1977), 419–421, for the soficity of the $\beta$-shift for Perron numbers.
