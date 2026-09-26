
# __Root Systems and Classification__

## Introduction

The structure theory of the companion article *Structure of Lie Algebras* decomposes a semisimple Lie algebra over a field of characteristic zero into simple ideals. This article describes the combinatorial invariant that classifies the simple algebras: the **root system**, a finite configuration of vectors in a Euclidean space, together with its **Dynkin diagram**. The passage from a simple Lie algebra to its root system is the root space decomposition with respect to a Cartan subalgebra; the passage back is the classification theorem of Killing and Cartan, which enumerates the possible root systems and finds exactly the four infinite families $A_n$, $B_n$, $C_n$, $D_n$ and the five exceptional algebras $G_2$, $F_4$, $E_6$, $E_7$, $E_8$.

The classification is the central result of the theory. It reduces a question about Lie algebras to a finite combinatorial computation: a connected Dynkin diagram is a graph of a restricted shape, and the list of such graphs is short and can be derived by h. Once the root system is known, the algebra is reconstructed, and with it the representation theory .

Throughout, $K$ is an algebraically closed field of characteristic zero, and $\mathfrak{g}$ is a finite-dimensional semisimple Lie algebra over $K$; the classification is a statement over such a field, and real forms and forms over other fields are mentioned only at the end. Lie algebras are written in lowercase fraktur, so $\mathfrak{g}$ is the algebra, $\mathfrak{h}$ a Cartan subalgebra, $\mathfrak{g}_\alpha$ a root space, and $\mathfrak{z}(\mathfrak{g})$ the centre; the field is $K$, $\mathbb{R}$ is used for the ambient Euclidean space of a root system, and the Killing form is $\kappa$, as in *Structure of Lie Algebras*. No physics is invoked.

## Cartan Subalgebras

### Definition and Existence

**Definition.** A **Cartan subalgebra** of a Lie algebra $\mathfrak{g}$ is a subalgebra $\mathfrak{h}$ that is nilpotent and equal to its own normaliser,

$$
\mathfrak{h} = N_{\mathfrak{g}}(\mathfrak{h}) = \{x \in \mathfrak{g} : [x, \mathfrak{h}] \subseteq \mathfrak{h}\}.
$$

**Theorem.** Every finite-dimensional Lie algebra over a field of characteristic zero has a Cartan subalgebra, and for a semisimple $\mathfrak{g}$ every Cartan subalgebra is abelian. Any two Cartan subalgebras of $\mathfrak{g}$ have the same dimension, the **rank** of $\mathfrak{g}$, and are conjugate under an automorphism of $\mathfrak{g}$.

**Proof sketch.** Existence is obtained by taking a maximal nilpotent subalgebra or, more elementarily, as the generalised eigenspace of a suitably generic element for eigenvalue zero. For semisimple $\mathfrak{g}$, a nilpotent subalgebra that equals its normaliser is abelian: if $\mathfrak{h}$ is nilpotent and $x \in [\mathfrak{h}, \mathfrak{h}]$, then $\operatorname{ad}_x$ is nilpotent on $\mathfrak{h}$, and the nondegeneracy of $\kappa$ on $\mathfrak{h}$ forces $x = 0$. Conjugacy is Chevalley's theorem; it is the algebraic form of the statement that all maximal tori of the corresponding group are conjugate. $\square$

**Example.** In $\mathfrak{sl}(n, K)$ the diagonal matrices of trace zero form a Cartan subalgebra $\mathfrak{h}$ of dimension $n - 1$. The rank of $\mathfrak{sl}(n)$ is therefore $n - 1$.

**Example.** In $\mathfrak{gl}(n, K)$ the diagonal matrices form a Cartan subalgebra, of dimension $n$; since $\mathfrak{gl}(n)$ is reductive rather than semisimple, its Cartan subalgebra need not lie in the derived subalgebra.

### Conjugacy and the Rank

The rank is an invariant of $\mathfrak{g}$, written $r = \operatorname{rank}\mathfrak{g} = \dim\mathfrak{h}$. For the simple algebras the rank and the algebra are related through the root system, and the classification below shows that the root system determines the algebra, so no further invariants are needed.

## The Root Space Decomposition

### Weights and Root Spaces

Let $\mathfrak{g}$ be semisimple, $\mathfrak{h}$ a Cartan subalgebra, and consider the action of the abelian algebra $\mathfrak{h}$ on $\mathfrak{g}$ by the adjoint map. Since the $\operatorname{ad}_h$ for $h \in \mathfrak{h}$ commute and are simultaneously diagonalisable over the algebraically closed field $K$, the algebra decomposes into common eigenspaces.

**Definition.** For $\alpha \in \mathfrak{h}^*$, the **root space** attached to $\alpha$ is

$$
\mathfrak{g}_\alpha = \{x \in \mathfrak{g} : [h, x] = \alpha(h)\, x \ \text{for all } h \in \mathfrak{h}\}.
$$

Since $\mathfrak{h}$ is abelian, $\mathfrak{h} \subseteq \mathfrak{g}_0$. A **root** of $\mathfrak{g}$ with respect to $\mathfrak{h}$ is a nonzero $\alpha \in \mathfrak{h}^*$ with $\mathfrak{g}_\alpha \neq 0$; the set of roots is written $\Phi \subseteq \mathfrak{h}^*$. The **root space decomposition** is

$$
\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha,
$$

the sum of the zero eigenspace $\mathfrak{g}_0 = \mathfrak{h}$ and the nonzero eigenspaces.

**Theorem.** Let $\mathfrak{g}$ be a semisimple Lie algebra over an algebraically closed field of characteristic zero, with Cartan subalgebra $\mathfrak{h}$. Then:

**(a)** $\Phi$ is finite, $0 \notin \Phi$, and $\Phi$ spans $\mathfrak{h}^*$;

**(b)** $\dim_K \mathfrak{g}_\alpha = 1$ and $\dim_K [\mathfrak{g}_\alpha, \mathfrak{g}_{-\alpha}] = 1$ for each $\alpha \in \Phi$;

**(c)** $\alpha \in \Phi$ implies $-\alpha \in \Phi$, and no other multiple of $\alpha$ is a root;

**(d)** $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subseteq \mathfrak{g}_{\alpha + \beta}$ for all $\alpha, \beta$, with the convention $\mathfrak{g}_\gamma = 0$ when $\gamma \notin \Phi \cup \{0\}$;

**(e)** $\kappa(\mathfrak{g}_\alpha, \mathfrak{g}_\beta) = 0$ unless $\alpha + \beta = 0$.

**Proof sketch.** Parts (c) and (d) are immediate from the definitions, and (e) follows from invariance of $\kappa$: for $x \in \mathfrak{g}_\alpha$, $y \in \mathfrak{g}_\beta$ and $h \in \mathfrak{h}$ one has $\alpha(h)\kappa(x, y) = \kappa([h, x], y) = -\kappa(x, [h, y]) = -\beta(h)\kappa(x, y)$, so $(\alpha + \beta)(h)\kappa(x, y) = 0$ for all $h$, and since the roots span $\mathfrak{h}^*$ this forces $\kappa(x, y) = 0$ unless $\alpha + \beta = 0$. Part (b) uses the representation theory of $\mathfrak{sl}(2)$: the subalgebra generated by $\mathfrak{g}_\alpha$ and $\mathfrak{g}_{-\alpha}$ is isomorphic to $\mathfrak{sl}(2, K)$, and the classification of its finite-dimensional modules over an algebraically closed field of characteristic zero forces both spaces to be one-dimensional. Part (a) then follows because $\mathfrak{g}$ is finite-dimensional and $\Phi$ spans $\mathfrak{h}^*$ (otherwise $\mathfrak{h}$ would not act faithfully on the sum of the root spaces). $\square$

### The Root Lattice and the Inner Product

The Killing form restricts to a nondegenerate symmetric form on $\mathfrak{h}$, and by invariance it is preserved by the adjoint action. For each $\alpha \in \mathfrak{h}^*$ there is a unique $t_\alpha \in \mathfrak{h}$ with

$$
\kappa(t_\alpha, h) = \alpha(h) \qquad \text{for all } h \in \mathfrak{h},
$$

and one transports the form to $\mathfrak{h}^*$ by

$$
(\alpha, \beta) = \kappa(t_\alpha, t_\beta).
$$

**Proposition.** The form $(\cdot, \cdot)$ on $\mathfrak{h}^*$ is symmetric and nondegenerate, and its restriction to the real span of the roots $\mathfrak{h}_{\mathbb{R}}^* = \operatorname{span}_{\mathbb{R}}\Phi$ is positive definite. Hence $\Phi$ is a finite configuration of vectors in a Euclidean space.

**Proof.** Symmetry and nondegeneracy are inherited from $\kappa$. That the real span is positive definite and that $(\alpha, \beta) \in \mathbb{Q}$ for roots is the content of the same $\mathfrak{sl}(2)$-computation that gives (b) above: the subalgebra generated by $\mathfrak{g}_\alpha$ and $\mathfrak{g}_{-\alpha}$ has the bracket relations of $\mathfrak{sl}(2)$ with $\alpha(h_\alpha) \in \mathbb{Q}$ and $(\alpha, \alpha) > 0$, and the form on the sum of the root lines is positive definite. $\square$

## Root Systems

### The Axioms

The abstract notion extracted from the decomposition is the following.

**Definition.** A **root system** in a finite-dimensional Euclidean space $E$ with inner product $(\cdot, \cdot)$ is a finite set $\Phi \subseteq E$ such that:

**(a)** $\Phi$ spans $E$ and $0 \notin \Phi$;

**(b)** for each $\alpha \in \Phi$ the **reflection** $s_\alpha : E \to E$,

$$
s_\alpha(\beta) = \beta - \frac{2(\beta, \alpha)}{(\alpha, \alpha)}\, \alpha,
$$

permutes $\Phi$;

**(c)** for all $\alpha, \beta \in \Phi$ the number $\dfrac{2(\beta, \alpha)}{(\alpha, \alpha)}$ is an integer.

A root system is **reduced** if for each $\alpha \in \Phi$ the only roots proportional to $\alpha$ are $\pm \alpha$, and **irreducible** if $\Phi$ cannot be partitioned into two nonempty orthogonal subsets.

**Theorem.** The set $\Phi$ of roots of a semisimple Lie algebra with respect to a Cartan subalgebra is a reduced root system in the Euclidean space $\mathfrak{h}_{\mathbb{R}}^*$.

**Proof.** Axiom (a) is part (a) of the root space decomposition theorem and the positive definiteness above. Axiom (b) is proved by exhibiting $s_\alpha$ as the reflection induced by the $\mathfrak{sl}(2)$-subalgebra generated by $\mathfrak{g}_{\pm\alpha}$: the automorphism $\exp(\operatorname{ad}_x)\exp(-\operatorname{ad}_y)\exp(\operatorname{ad}_x)$ for suitable $x, y$ acts on $\mathfrak{h}^*$ by $s_\alpha$. Axiom (c) follows because the eigenvalues of $\operatorname{ad}_{h_\alpha}$ on $\mathfrak{g}_\beta$ are integers, the representation being the restriction of a finite-dimensional $\mathfrak{sl}(2)$-module. Reducedness is part (c) of the decomposition theorem. $\square$

### The Weyl Group

**Definition.** The **Weyl group** of $\Phi$ is the subgroup $W \subseteq O(E)$ generated by the reflections $s_\alpha$ for $\alpha \in \Phi$. It is finite, since it permutes the finite set $\Phi$.

**Proposition.** $W$ is a finite reflection group, and $\Phi$ is stable under $W$. The Weyl group is the group of automorphisms of $\Phi$ generated by the reflections, and it acts faithfully on $E$.

**Example.** For $A_n$ the Weyl group is the symmetric group $S_{n+1}$, acting on the coordinates of $\mathbb{R}^{n+1}$; for $B_n$ and $C_n$ it is the hyperoctahedral group $(\mathbb{Z}/2)^n \rtimes S_n$ of signed permutations; for $D_n$ it is the subgroup of signed permutations with an even number of sign changes; and for $G_2$ it is the dihedral group of order $12$.

### Angles and Lengths

The integer in axiom (c) is written

$$
\langle \beta, \alpha^\vee \rangle = \frac{2(\beta, \alpha)}{(\alpha, \alpha)},
$$

where $\alpha^\vee = 2\alpha/(\alpha, \alpha)$ is the **coroot**, and the axiom says $\langle \beta, \alpha^\vee \rangle \in \mathbb{Z}$.

**Proposition.** For non-proportional roots $\alpha, \beta$ with $(\alpha, \alpha) \geq (\beta, \beta)$, the positive integer

$$
\langle \alpha, \beta^\vee \rangle \langle \beta, \alpha^\vee \rangle = 4\cos^2\theta
$$

takes one of the values $0, 1, 2, 3$, where $\theta$ is the angle between $\alpha$ and $\beta$; the value $4$ occurs only for proportional roots. Consequently the possible angles between distinct non-proportional roots are $90^\circ$, $60^\circ$ or $120^\circ$, $45^\circ$ or $135^\circ$, and $30^\circ$ or $150^\circ$, and if $(\alpha, \alpha) \neq (\beta, \beta)$ the ratio of the squared lengths is $2$ or $3$ (or $1/2, 1/3$).

**Proof.** Since $s_\alpha(\beta) - \beta = -\langle\beta,\alpha^\vee\rangle\alpha$ and $s_\alpha$ preserves length, the two integers $m = \langle\beta,\alpha^\vee\rangle$ and $n = \langle\alpha,\beta^\vee\rangle$ satisfy $mn = 4\cos^2\theta \geq 0$, and $|\cos\theta| < 1$ for non-proportional roots, so $mn \in \{0, 1, 2, 3\}$. The length ratio is $(\alpha,\alpha)/(\beta,\beta) = n/m$ when $m \neq 0$, which gives the stated possibilities. $\square$

## Simple Roots and the Cartan Matrix

### Positive Systems and Simple Roots

**Definition.** Choose $t \in E$ with $(\alpha, t) \neq 0$ for every $\alpha \in \Phi$, and call a root $\alpha$ **positive** if $(\alpha, t) > 0$; write $\Phi^+$ for the positive roots and $\Phi^- = -\Phi^+$. The **simple roots** are the positive roots that cannot be written as a sum of two positive roots; their set is written $\Pi = \{\alpha_1, \ldots, \alpha_r\}$.

**Theorem.** The simple roots form a basis of $E$; every positive root is a nonnegative integer combination of simple roots, and every root is an integer combination with coefficients all of the same sign (or zero). The number of simple roots is $r = \dim\mathfrak{h}$, the rank of $\mathfrak{g}$, and $|\Phi^+| = \tfrac{1}{2}|\Phi|$.

**Proof.** That $\Pi$ is linearly independent and generates the root lattice is standard; the sign-coherent expression is obtained by induction on the height $(\alpha, t)$. The last statement follows because $\Phi^- = -\Phi^+$. $\square$

**Proposition.** For distinct simple roots $\alpha_i, \alpha_j$ one has $(\alpha_i, \alpha_j) \leq 0$, and $\langle \alpha_j, \alpha_i^\vee \rangle \in \{0, -1, -2, -3\}$.

**Proof.** If $(\alpha_i, \alpha_j) > 0$ for two simple roots, then $s_{\alpha_i}(\alpha_j) = \alpha_j - \langle\alpha_j, \alpha_i^\vee\rangle\alpha_i$ is a root, and the coefficient of $\alpha_i$ has the opposite sign to that of $\alpha_j$ in the simple-root expansion; choosing the signs appropriately produces a positive root that is a difference of simple roots, contradicting their simplicity. $\square$

### The Cartan Matrix

**Definition.** The **Cartan matrix** of $\Phi$ relative to the ordered simple system $(\alpha_1, \ldots, \alpha_r)$ is the integer matrix $A = (a_{ij})$ with

$$
a_{ij} = \langle \alpha_j, \alpha_i^\vee \rangle = \frac{2(\alpha_i, \alpha_j)}{(\alpha_i, \alpha_i)}.
$$

**Proposition.** The Cartan matrix has the following properties:

**(a)** $a_{ii} = 2$ for all $i$;

**(b)** $a_{ij} \in \{0, -1, -2, -3\}$ for $i \neq j$;

**(c)** $a_{ij} = 0$ if and only if $a_{ji} = 0$;

**(d)** $A$ is symmetrisable: $DA$ is symmetric for the diagonal matrix $D = \operatorname{diag}((\alpha_1, \alpha_1), \ldots, (\alpha_r, \alpha_r))$, and $DA$ is positive definite;

**(e)** every proper principal submatrix of $A$ is a Cartan matrix of a smaller root system, and $\det A > 0$.

**Proof.** (a) is immediate. (b) is the proposition above read through the definition. (c) follows because $a_{ij} = 0$ is equivalent to $(\alpha_i, \alpha_j) = 0$. For (d), $D A$ has entries $2(\alpha_i, \alpha_j)$, which is symmetric and, being the matrix of the restriction of the positive definite form to a basis, positive definite. (e) is the statement that a subsystem of simple roots spans a sub-root-system, standard from the classification. $\square$

### The Dynkin Diagram

**Definition.** The **Dynkin diagram** of a root system with simple system $(\alpha_1, \ldots, \alpha_r)$ is the graph with one node for each simple root, two nodes $i \neq j$ joined by $a_{ij}a_{ji}$ edges (so $0$, $1$, $2$ or $3$), and an arrow on a double or triple edge pointing from the longer root to the shorter one.

**Proposition.** The root system is irreducible if and only if its Dynkin diagram is connected, and it is the direct sum of the root systems of the components otherwise. The Dynkin diagram determines the Cartan matrix and hence the root system.

**Proof.** If $\Phi$ decomposes into two orthogonal parts, so does the simple system, and the diagram is disconnected; conversely a disconnected diagram gives orthogonal subsets. The reconstruction of $A$ from the diagram uses the length ratio encoded by the arrow together with the integer $a_{ij}a_{ji}$. $\square$

## The Classification

### The Classification Theorem

**Theorem (Killing–Cartan).** The connected Dynkin diagrams are exactly

$$
A_n\ (n \geq 1), \quad B_n\ (n \geq 2), \quad C_n\ (n \geq 3), \quad D_n\ (n \geq 4), \quad E_6,\ E_7,\ E_8,\ F_4,\ G_2,
$$

with the low-rank coincidences $B_2 = C_2$, $A_3 = D_3$, and $A_1 = B_1 = C_1$ resolved by convention. Consequently there is a bijection between isomorphism classes of simple Lie algebras over an algebraically closed field of characteristic zero, connected Dynkin diagrams, and irreducible reduced root systems.

**Proof sketch.** The reduction is a combinatorial computation on the Cartan matrix. From the properties above, the matrix $DA$ is positive definite with diagonal $2$ and off-diagonal entries nonpositive integers, and such matrices with connected diagram are classified by considering the possible subdiagrams: any diagram containing a cycle or a node of degree at least $4$ is excluded by positive definiteness, and a case check on the remaining graphs yields exactly the list. The reconstruction of the algebra from the root system uses Serre's construction: the Lie algebra is the quotient of the free Lie algebra on generators $e_i, f_i, h_i$ by the Serre relations determined by the Cartan matrix, and the axioms of the root system ensure that this quotient is finite-dimensional, semisimple and has the given roots. $\square$

### The Classical Types

The four infinite families are realised by the classical matrix algebras, whose root systems are most conveniently written down using the standard orthonormal basis $e_1, \ldots, e_m$ of $\mathbb{R}^m$.

| Type | Algebra | Root system $\Phi$ | Rank | $\dim\mathfrak{g} = r + \vert\Phi\vert$ | Weyl group |
|---|---|---|---|---|---|
| $A_n$ | $\mathfrak{sl}(n+1, K)$ | $\pm(e_i - e_j)$, $1 \leq i < j \leq n+1$ | $n$ | $n(n+2)$ | $S_{n+1}$ |
| $B_n$ | $\mathfrak{so}(2n+1, K)$ | $\pm e_i$, $\pm e_i \pm e_j$ | $n$ | $n(2n+1)$ | $(\mathbb{Z}/2)^n \rtimes S_n$ |
| $C_n$ | $\mathfrak{sp}(2n, K)$ | $\pm 2e_i$, $\pm e_i \pm e_j$ | $n$ | $n(2n+1)$ | $(\mathbb{Z}/2)^n \rtimes S_n$ |
| $D_n$ | $\mathfrak{so}(2n, K)$ | $\pm e_i \pm e_j$ | $n$ | $n(2n-1)$ | $(\mathbb{Z}/2)^{n-1} \rtimes S_n$ |

The counts of roots are $n(n+1)$ for $A_n$, $2n^2$ for $B_n$, $2n^2$ for $C_n$, and $2n(n-1)$ for $D_n$, giving the dimensions in the table. The simple roots can be chosen as:

$$
A_n: \ \alpha_i = e_i - e_{i+1}; \qquad B_n: \ \alpha_i = e_i - e_{i+1}\ (i < n), \ \alpha_n = e_n;
$$

$$
C_n: \ \alpha_i = e_i - e_{i+1}\ (i < n), \ \alpha_n = 2e_n; \qquad D_n: \ \alpha_i = e_i - e_{i+1}\ (i < n), \ \alpha_n = e_{n-1} + e_n.
$$

### The Exceptional Types

The five exceptional diagrams carry the following data.

| Type | Rank | Number of roots | $\dim\mathfrak{g}$ | $\det$ of Cartan matrix |
|---|---|---|---|---|
| $G_2$ | $2$ | $12$ | $14$ | $1$ |
| $F_4$ | $4$ | $48$ | $52$ | $1$ |
| $E_6$ | $6$ | $72$ | $78$ | $3$ |
| $E_7$ | $7$ | $126$ | $133$ | $2$ |
| $E_8$ | $8$ | $240$ | $248$ | $1$ |

The dimensions are $r + |\Phi|$ as for the classical types. The determinant of the Cartan matrix is the index of connection of the root lattice in the weight lattice; it is $1$ for $G_2$, $F_4$ and $E_8$, which are simply connected with both lattices equal, and $2$ or $3$ for $E_7$ and $E_6$. The Weyl group orders are $12$ for $G_2$, $1152$ for $F_4$, $51840$ for $E_6$, $2903040$ for $E_7$, and $696729600$ for $E_8$.

## Examples

### The Root System $A_2$

Let $\mathfrak{g} = \mathfrak{sl}(3, K)$ with Cartan subalgebra $\mathfrak{h}$ the diagonal traceless matrices, described in the coordinates $h = \operatorname{diag}(a_1, a_2, a_3)$ with $a_1 + a_2 + a_3 = 0$. The roots are

$$
\Phi = \{ \pm(e_1 - e_2), \pm(e_1 - e_3), \pm(e_2 - e_3) \},
$$

where $e_i(h) = a_i$; they lie in the plane $\sum_i e_i = 0$, and there are six of them. The root spaces are the lines spanned by the matrix units, $\mathfrak{g}_{e_i - e_j} = \langle E_{ij}\rangle$. Choosing $t$ so that $e_1 - e_2$ and $e_2 - e_3$ are positive gives the simple system

$$
\alpha_1 = e_1 - e_2, \qquad \alpha_2 = e_2 - e_3, \qquad \alpha_1 + \alpha_2 = e_1 - e_3,
$$

with Cartan matrix

$$
A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix},
$$

and Dynkin diagram $A_2$, the path with two nodes joined by a single edge. The Weyl group is $S_3$, of order $6$, generated by the reflections in the two simple roots; the algebra has dimension $\dim\mathfrak{h} + |\Phi| = 2 + 6 = 8$, as expected for $\mathfrak{sl}(3)$.

### The Root System $A_n$ in General

For $\mathfrak{sl}(n+1, K)$ the Cartan subalgebra is the traceless diagonal matrices and the roots are $e_i - e_j$ for $i \neq j$, acting by $h \mapsto a_i - a_j$. The root spaces are the lines $\langle E_{ij}\rangle$, and the simple roots are $\alpha_i = e_i - e_{i+1}$ for $i = 1, \ldots, n$. The Cartan matrix has $2$ on the diagonal, $-1$ on the sub- and super-diagonal, and $0$ elsewhere, so the Dynkin diagram is the path $A_n$. The root system is realised in the hyperplane $\sum_i a_i = 0$ of $\mathbb{R}^{n+1}$; the Weyl group is $S_{n+1}$, acting by permuting the coordinates, and the number of roots is $n(n+1)$, so $\dim\mathfrak{sl}(n+1) = n + n(n+1) = n(n+2) = (n+1)^2 - 1$, as it must be.

**Remark (fields other than $K$).** Over a field that is not algebraically closed, a simple Lie algebra over the algebraic closure may carry several inequivalent descended forms; over $\mathbb{R}$ these are the **real forms**, classified by Satake diagrams, of which the compact and split forms are the extremes. The classification above is the classification over the algebraic closure, and the descended forms are a further, finite layer of the theory.

## Summary

A semisimple Lie algebra $\mathfrak{g}$ over an algebraically closed field of characteristic zero has a Cartan subalgebra $\mathfrak{h}$, abelian, self-normalising, of dimension equal to the rank $r$ of $\mathfrak{g}$, and unique up to conjugacy. The adjoint action of $\mathfrak{h}$ gives the root space decomposition

$$
\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha,
$$

with each root space one-dimensional, $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subseteq \mathfrak{g}_{\alpha+\beta}$, and $-\alpha \in \Phi$ whenever $\alpha \in \Phi$. Transporting the Killing form to $\mathfrak{h}^*$ makes $\Phi$ a reduced root system in a Euclidean space: finite, spanning, stable under the reflections $s_\alpha$, with integrality of $2(\beta,\alpha)/(\alpha,\alpha)$.

Choosing a positive system gives the simple roots, a basis of $\mathfrak{h}^*$ with the Cartan matrix $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$, symmetrisable and positive definite, whose Dynkin diagram encodes the system. The connected Dynkin diagrams are $A_n$, $B_n$, $C_n$, $D_n$, $E_6$, $E_7$, $E_8$, $F_4$, $G_2$, by the theorem of Killing and Cartan, and this list is in bijection with the simple Lie algebras over the algebraic closure and with the irreducible reduced root systems. The classical types are realised by $\mathfrak{sl}(n+1)$, $\mathfrak{so}(2n+1)$, $\mathfrak{sp}(2n)$ and $\mathfrak{so}(2n)$, with the dimensions and Weyl groups of the tables; the root system, the Cartan matrix and the Dynkin diagram determine the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Algebraically closed field of characteristic zero |
| $\mathfrak{g}$ | Finite-dimensional semisimple Lie algebra over $K$ |
| $\mathfrak{h}$ | Cartan subalgebra; abelian, self-normalising, of dimension the rank $r$ |
| $r = \operatorname{rank}\mathfrak{g}$ | $\dim\mathfrak{h}$ |
| $\mathfrak{g}_\alpha$ | Root space $\{x : [h,x] = \alpha(h)x \ \forall h \in \mathfrak{h}\}$ |
| $\Phi \subseteq \mathfrak{h}^*$ | Root system; $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi}\mathfrak{g}_\alpha$ |
| $\kappa$ | Killing form; its transport to $\mathfrak{h}^*$ is $(\cdot, \cdot)$ |
| $(\cdot, \cdot)$ | Positive definite form on $\mathfrak{h}^*$ making $\Phi$ a root system |
| $s_\alpha(\beta) = \beta - \frac{2(\beta,\alpha)}{(\alpha,\alpha)}\alpha$ | Reflection in a root |
| $\alpha^\vee = 2\alpha/(\alpha,\alpha)$ | Coroot |
| $\langle \beta, \alpha^\vee \rangle = 2(\beta,\alpha)/(\alpha,\alpha)$ | Pairing, an integer for roots |
| $W$ | Weyl group, generated by the reflections $s_\alpha$ |
| $\Phi^+, \Pi = \{\alpha_1, \ldots, \alpha_r\}$ | Positive roots and simple roots |
| $A = (a_{ij})$, $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$ | Cartan matrix |
| $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$ | The connected Dynkin diagrams |
| $\mathfrak{sl}(n+1), \mathfrak{so}(2n+1), \mathfrak{sp}(2n), \mathfrak{so}(2n)$ | Classical algebras of types $A_n, B_n, C_n, D_n$ |



## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for Cartan subalgebras, root systems, and the classification theorem.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 1987), for the root space decomposition and Serre's construction of the algebra from its Cartan matrix.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the conjugacy of Cartan subalgebras and the structure of the root lattice.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6* (Springer, 2002), for root systems, Weyl groups, and the classification of Dynkin diagrams.
- James E. Humphreys, *Reflection Groups and Coxeter Groups* (Cambridge University Press, 1990), for finite reflection groups and the Weyl group in its own right.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for root systems in the setting of symmetric spaces and real forms.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the classification over $\mathbb{C}$ and its consequences for representations.
