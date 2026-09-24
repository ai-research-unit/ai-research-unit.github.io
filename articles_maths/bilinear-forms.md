
# __Bilinear Forms__

## Introduction

A **bilinear form** on a module is a rule that assigns to two vectors a scalar, linearly in each vector separately. This article develops the theory of such forms over a commutative ring: the basic definition, the matrix that represents a form in a basis, the radical and non-degeneracy, orthogonal direct sums, and the alternating case. It fixes the vocabulary used by the rest of the category.

The treatment is purely mathematical, and the default base is a **commutative ring** $R$ with identity $1 \neq 0$. Modules over a ring need not be free, so a form need not have a matrix; when it does, invertibility of the matrix has to be read in the ring-theoretic sense. Two hypotheses recur and are flagged wherever they are used: the ring may be required to be a field, and the element $2$ may be required to be invertible. We assume familiarity with modules and linear maps as in *Modules*, and with the tensor and exterior constructions as in *Algebras: A General Introduction*. Quadratic forms, and the passage between a quadratic form and the symmetric bilinear form that polarises it, are not covered here; a bilinear form here is the datum, not yet a quadratic form.

## Bilinear Forms

### Definition

Let $M$ be an $R$-module. A **bilinear form** on $M$ is a function

$$
B : M \times M \longrightarrow R
$$

that is additive and $R$-linear in each argument separately:

$$
B(u + v, w) = B(u, w) + B(v, w), \qquad B(ru, v) = r\,B(u, v),
$$

$$
B(u, v + w) = B(u, v) + B(u, w), \qquad B(u, rv) = r\,B(u, v),
$$

for all $u, v, w \in M$ and $r \in R$. Equivalently, $B$ is an $R$-linear map $M \otimes_R M \to R$, and the two descriptions are related by $B(u \otimes v) = B(u, v)$; when $M$ is free this is the same as a bilinear function in the elementary sense.

The set of all bilinear forms on $M$ is an $R$-module under pointwise addition and scalar multiplication, written $\operatorname{Bil}_R(M)$.

**Example.** On $M = R^n$ the **standard dot product**

$$
B(x, y) = \sum_{i=1}^{n} x_i y_i
$$

is bilinear. On $M = R^2$ the function $B((x_1, y_1), (x_2, y_2)) = x_1 y_2 + y_1 x_2$ is bilinear, and it satisfies $B(v, v) = 2 x_1 y_1$, which vanishes on the vector $(1, 0)$ but not on $(1, 1)$.

**Example.** For the $\mathbb{Z}$-module $\mathbb{Z}^2$ the determinant

$$
B\bigl((x_1, y_1), (x_2, y_2)\bigr) = x_1 y_2 - y_1 x_2
$$

is bilinear, and it is skew-symmetric; it is alternating, since $B(v, v) = 0$ for every $v$.

### Symmetric, Alternating and Skew-Symmetric Forms

Three symmetry conditions single out the forms that matter.

**Definition.** A bilinear form $B$ on $M$ is

- **symmetric** if $B(u, v) = B(v, u)$ for all $u, v \in M$;
- **skew-symmetric** if $B(u, v) = -B(v, u)$ for all $u, v \in M$;
- **alternating** if $B(v, v) = 0$ for all $v \in M$.

**Proposition.** Every alternating form is skew-symmetric. If $2$ is invertible in $R$, the converse holds, and a form that is both symmetric and skew-symmetric is zero.

**Proof.** If $B$ is alternating, expanding $B(u + v, u + v) = 0$ by bilinearity gives

$$
0 = B(u, u) + B(u, v) + B(v, u) + B(v, v) = B(u, v) + B(v, u),
$$

so $B(u, v) = -B(v, u)$ and $B$ is skew-symmetric. Conversely, if $B$ is skew-symmetric then $B(v, v) = -B(v, v)$, that is $2 B(v, v) = 0$, and invertibility of $2$ gives $B(v, v) = 0$. If $B$ is both symmetric and skew-symmetric then $B(u, v) = B(v, u) = -B(u, v)$, so $2B(u, v) = 0$ and again $B = 0$ when $2$ is invertible. $\square$

**Remark.** Over a ring in which $2$ is not invertible the three notions genuinely differ. Over $\mathbb{F}_2$ the form $B(x, y) = xy$ on $\mathbb{F}_2$ is symmetric because $-1 = 1$, but it is not alternating, since $B(1, 1) = 1$. Symmetric and alternating forms are therefore not interchangeable in characteristic $2$.

We work with symmetric and alternating forms throughout. The skew-symmetric forms are recovered from the alternating ones when $2$ is invertible, and in that case the classification of skew-symmetric forms is the classification of alternating forms.

### The Matrix of a Form

Let $M$ be **free** of finite rank $n$ with basis $e_1, \ldots, e_n$. A bilinear form is determined by its values on pairs of basis vectors, so define

$$
G_{ij} = B(e_i, e_j), \qquad G = (G_{ij}) \in M_n(R).
$$

For $u = \sum_i u_i e_i$ and $v = \sum_j v_j e_j$, bilinearity gives

$$
B(u, v) = \sum_{i=1}^{n} \sum_{j=1}^{n} u_i v_j\, B(e_i, e_j) = [u]^T G\, [v],
$$

where $[u]$ and $[v]$ are the coordinate columns. The matrix $G$ is the **Gram matrix** of $B$ in the basis, and the assignment $B \mapsto G$ is an isomorphism of $R$-modules $\operatorname{Bil}_R(M) \to M_n(R)$.

**Proposition.** The form $B$ is symmetric if and only if $G = G^T$, and skew-symmetric if and only if $G = -G^T$. It is alternating if and only if $G = -G^T$ and every diagonal entry of $G$ is zero.

**Proof.** The first two statements are immediate from $B(e_i, e_j) = G_{ij}$ and the symmetry conditions. For the third, $G = -G^T$ is equivalent to skew-symmetry, and the diagonal entries are $G_{ii} = B(e_i, e_i)$; these vanish for all $i$ if and only if $B(v, v) = 0$ for every $v$, since $B(v, v) = \sum_i v_i^2 G_{ii}$ when $B$ is skew-symmetric. $\square$

Two bases give two Gram matrices, related by a change of basis.

**Proposition.** Let $\mathcal{B}$ and $\mathcal{B}'$ be bases of $M$, and let $P$ be the change-of-basis matrix defined by $[v]_{\mathcal{B}} = P\,[v]_{\mathcal{B}'}$. If $G$ and $G'$ are the Gram matrices in the two bases, then

$$
G' = P^T G\, P.
$$

**Proof.** Substituting $[u]_{\mathcal{B}} = P[u]_{\mathcal{B}'}$ and $[v]_{\mathcal{B}} = P[v]_{\mathcal{B}'}$ into $B(u, v) = [u]_{\mathcal{B}}^T G [v]_{\mathcal{B}}$ gives

$$
B(u, v) = [u]_{\mathcal{B}'}^T \bigl(P^T G P\bigr) [v]_{\mathcal{B}'},
$$

and the Gram matrix in $\mathcal{B}'$ is the matrix appearing in the middle. $\square$

**Definition.** Two matrices $G, G' \in M_n(R)$ are **congruent** if $G' = P^T G P$ for some invertible $P$; two bilinear forms on a free module are congruent when their Gram matrices are related in this way in some pair of bases. Congruence is an equivalence relation, and classifying bilinear forms on a free module of rank $n$ up to congruence is the same as classifying forms up to change of basis.

## Rank and the Radical

### Rank

Let $B$ be a bilinear form on a free module $M$ of finite rank, with Gram matrix $G$ in some basis. The **rank** of $B$ is

$$
\operatorname{rank}(B) = \operatorname{rank}(G),
$$

the rank of the matrix $G$, that is the largest size of an invertible minor. The rank is independent of the basis: a change of basis replaces $G$ by $P^T G P$ with $P$ invertible, and multiplication by invertible matrices preserves rank. Over a field we also have the rank–nullity reading of the next subsection.

### Orthogonality

Two vectors $u, v \in M$ are **orthogonal** with respect to $B$, written $u \perp v$, if $B(u, v) = 0$. For a subset $S \subseteq M$, its **orthogonal complement** is

$$
S^\perp = \{u \in M : B(u, s) = 0 \text{ for all } s \in S\}.
$$

The complement $S^\perp$ is a submodule of $M$. For a symmetric or skew-symmetric form the relation of orthogonality is symmetric in $u$ and $v$, and then $S \subseteq (S^\perp)^\perp$. In general the two-sided orthogonal complement may be larger than $S$; the radical defined below measures the failure.

### The Radical

For a bilinear form $B$ on $M$, the **radical** is

$$
\operatorname{rad}(B) = \{u \in M : B(u, v) = 0 \text{ for all } v \in M\} = M^\perp.
$$

It is the kernel of the induced linear map

$$
M \longrightarrow M^*, \qquad u \longmapsto B(u, -),
$$

where $M^* = \operatorname{Hom}_R(M, R)$ is the dual module. For a symmetric or skew-symmetric form the left radical $\{u : B(v, u) = 0\ \forall v\}$ coincides with the right radical $\operatorname{rad}(B)$.

**Proposition.** Let $M$ be free of rank $n$, with Gram matrix $G$. Then $\operatorname{rad}(B)$ is the kernel of the map $R^n \to R^n$ given by $x \mapsto G^{T}x$ in coordinates, and the following are equivalent:

1. $\operatorname{rad}(B) = 0$;
2. the map $M \to M^*$, $u \mapsto B(u, -)$, is injective;
3. $\det G$ is not a zero divisor of $R$.

**Proof.** In coordinates the map $u \mapsto B(u, -)$ sends $x$ to the functional $y \mapsto x^T G y$, that is to the row vector $x^T G$, whose transpose is $G^T x$. Its kernel is $\operatorname{rad}(B)$, and for a symmetric or skew-symmetric form it is also the kernel of $x \mapsto Gx$, since $G^T$ then differs from $\pm G$. Statement 3 is the condition that the square matrix $G$ have no nonzero kernel vector, a condition equivalent to $\det G$ being a non-zero-divisor; this equivalence is a standard corollary of McCoy's theorem for matrices over a commutative ring. $\square$

### Non-Degenerate Forms

**Definition.** A bilinear form $B$ on $M$ is **non-degenerate** if the map $M \to M^*$, $u \mapsto B(u, -)$, is an isomorphism. It is **degenerate** otherwise.

Over a general commutative ring non-degeneracy is strictly stronger than the vanishing of the radical: it requires the map to be surjective as well as injective.

**Proposition.** Let $M$ be free of finite rank with Gram matrix $G$. Then $B$ is non-degenerate if and only if $\det G$ is a **unit** of $R$.

**Proof.** The map $M \to M^*$ is represented by $G$, and an endomorphism of a free module of finite rank is an isomorphism if and only if its determinant is a unit. $\square$

**Example.** Let $R = \mathbb{R}$ and $G = \operatorname{diag}(1, 1, 0)$ on $\mathbb{R}^3$. Then $G$ has rank $2$ and radical spanned by $e_3$, so the form is degenerate. Let $R = \mathbb{Z}$ and $G = (2)$ on $\mathbb{Z}$. Then $\det G = 2$ is not a unit, the radical is zero, and the map $\mathbb{Z} \to \mathbb{Z}^*$ is multiplication by $2$, which is injective but not surjective: the form is degenerate although its radical vanishes.

**Remark (the field case).** Over a field, and for a finite-dimensional space, the dual has the same dimension, so injectivity of $M \to M^*$ is equivalent to bijectivity, and the following are equivalent:

1. $B$ is non-degenerate;
2. $\operatorname{rad}(B) = 0$;
3. the Gram matrix $G$ in any basis is invertible;
4. $\dim M = \operatorname{rank}(B)$.

The equivalence of 2 and 4 gives $\dim \operatorname{rad}(B) = \dim M - \operatorname{rank}(B)$ over a field.

**Remark (the infinite-dimensional case).** Over an infinite-dimensional vector space, injectivity is again not equivalent to bijectivity. If $M = \bigoplus_{\mathbb{N}} R$ with $B(e_i, e_j) = \delta_{ij}$, the radical is zero, since $B(v, e_i) = 0$ for all $i$ forces every coordinate of $v$ to vanish; but the functional taking the value $1$ on every basis vector is not of the form $B(v, -)$, because such a $v$ would need infinitely many nonzero coordinates and $M$ consists of finite sums. So the radical vanishes while the form is degenerate.

### Restriction and Orthogonal Direct Sums

**Definition.** Let $M_1, M_2$ be $R$-modules carrying bilinear forms $B_1, B_2$. The **orthogonal direct sum** $B_1 \perp B_2$ is the form on $M_1 \oplus M_2$ defined by

$$
(B_1 \perp B_2)\bigl((u_1, u_2), (v_1, v_2)\bigr) = B_1(u_1, v_1) + B_2(u_2, v_2).
$$

**Proposition.** The orthogonal direct sum $B_1 \perp B_2$ is symmetric, skew-symmetric or alternating if and only if both summands are. It is non-degenerate if and only if both summands are, and its Gram matrix in the concatenated basis is the block sum $\operatorname{diag}(G_1, G_2)$.

**Proof.** The symmetry statements are immediate. The subspace $M_1$ is orthogonal to $M_2$, so the radical of $B_1 \perp B_2$ is $\operatorname{rad}(B_1) \oplus \operatorname{rad}(B_2)$, and the map to the dual is the direct sum of the two maps. Hence it is an isomorphism exactly when both factors are. The Gram matrix is block diagonal by construction. $\square$

The restriction of a non-degenerate form to a general submodule need not be non-degenerate. Over a field, however, the situation is controlled.

**Proposition.** Let $B$ be non-degenerate on a finite-dimensional space $V$ over a field, and let $W \subseteq V$ be a subspace. Then

$$
\dim W + \dim W^\perp = \dim V, \qquad W \subseteq (W^\perp)^\perp,
$$

and the following are equivalent: (i) $V = W \perp W^\perp$; (ii) $W \cap W^\perp = 0$; (iii) the restriction of $B$ to $W$ is non-degenerate.

**Proof.** The map $V \to W^*$, $v \mapsto B(v, -)|_W$, has kernel $W^\perp$, and it is surjective: a functional on $W$ extends to a functional on $V$, and non-degeneracy of $B$ realises that extension as $B(v, -)$. Hence $\dim W^\perp = \dim V - \dim W$. The same formula applied to $W^\perp$ gives $\dim (W^\perp)^\perp = \dim W$, and since $W \subseteq (W^\perp)^\perp$ always, the inclusion is an equality. A vector of $W \cap W^\perp$ is orthogonal to all of $W$ and to all of $W^\perp$, hence to all of $V$, so $W \cap W^\perp = 0$ because $B$ is non-degenerate; consequently $W + W^\perp = V$ by the dimension formula. The three conditions are now equivalent: the radical of the restriction of $B$ to $W$ is $W \cap W^\perp$, so (ii) and (iii) hold or fail together, and they hold exactly when $W + W^\perp = V$, which is (i). $\square$

**Remark.** Over a ring, the proof fails at the step that extends a functional from $W$ to $V$: the extension need not be of the form $B(v, -)$, and the dimension formula can fail. This is the source of the additional hypotheses in the ring version of the extension theorem and in the discussion of forms with values in an algebra.

## Alternating Forms

### Alternating Forms Have Even Rank

Alternating forms behave more rigidly than symmetric ones.

**Proposition.** Let $B$ be an alternating form on a free module of finite rank over a ring in which $2$ is invertible. If $B$ is non-degenerate, the rank of the module is even.

**Proof.** The Gram matrix satisfies $G = -G^T$. Taking determinants, $\det G = \det(-G^T) = (-1)^n \det G$, where $n$ is the rank. Hence $2 \det G = 0$ when $n$ is odd. Since $2$ is invertible this gives $\det G = 0$, contradicting non-degeneracy. $\square$

Over a field the same argument shows that the rank of any alternating form is even: the radical is orthogonal to all of $V$, so $V = W \perp \operatorname{rad}(B)$ with $W$ carrying a non-degenerate alternating form of dimension $\operatorname{rank}(B)$, to which the proposition applies.

### The Symplectic Basis

**Theorem (standard normal form).** Let $B$ be a non-degenerate alternating form on a finite-dimensional vector space $V$ over a field. Then $\dim V = 2m$ for some $m$, and there is a basis

$$
e_1, \ldots, e_m, f_1, \ldots, f_m
$$

such that

$$
B(e_i, e_j) = 0, \qquad B(f_i, f_j) = 0, \qquad B(e_i, f_j) = \delta_{ij}.
$$

In the ordering $e_1, f_1, \ldots, e_m, f_m$ the Gram matrix is the block sum of $m$ copies of $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$; in the ordering $e_1, \ldots, e_m, f_1, \ldots, f_m$, which is the one used, it is the block matrix $\begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$ with $I_m$ the identity matrix of size $m$.

**Proof sketch.** If $B \neq 0$ there are $u, v$ with $c = B(u, v) \neq 0$, and $u, v$ are independent because $B$ is alternating; replacing $v$ by $v/c$, which is legal over a field, gives $B(e_1, f_1) = 1$ for $e_1 = u$ and $f_1 = v/c$. The plane $H_1 = \operatorname{span}\{e_1, f_1\}$ is non-degenerate, so $V = H_1 \perp H_1^\perp$ by the restriction proposition, and $H_1^\perp$ carries a non-degenerate alternating form of dimension $\dim V - 2$; induction on $\dim V$ finishes. $\square$

**Definition.** A basis with the property above is a **symplectic basis**, and the form is **hyperbolic** when it has such a basis. Two non-degenerate alternating forms of the same dimension over a field are isometric, because each can be put in symplectic form; the alternation case therefore has a single invariant, the dimension, once non-degeneracy is assumed.

**Example (the symplectic plane).** On $R^2$ the form

$$
B\bigl((x_1, y_1), (x_2, y_2)\bigr) = x_1 y_2 - y_1 x_2, \qquad G = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

is alternating and non-degenerate, and the vectors $u = (1, 0)$ and $v = (0, 1)$ satisfy $B(u, v) = 1$. It is the two-dimensional case of the normal form and the elementary block of the symplectic theory. The name **hyperbolic plane** is used in this category for the quadratic space, whose polar form in a basis $e, f$ with $q(e) = q(f) = 0$ and $B(e, f) = 1$ is the symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$; the two-dimensional alternating space above is a different object, and the symbol $H$ denotes the quadratic one. The same symmetric matrix, with $2$ invertible, is the symmetric form $\langle 1, -1\rangle$ in a suitable basis, and it is not alternating, by the proposition above relating alternating and skew-symmetric forms.

## Isometries

### Definition

Let $B$ be a bilinear form on $M$ and $B'$ a bilinear form on $M'$. An **isometry** from $B$ to $B'$ is an $R$-linear isomorphism $T : M \to M'$ with

$$
B'(Tu, Tv) = B(u, v) \qquad (u, v \in M).
$$

An isometry of $B$ with itself is an **isometry of $B$**, and the isometries of $B$ form a group under composition, the **isometry group** $\operatorname{Isom}(M, B)$.

In a basis an isometry is a matrix $P$ with $P^T G' P = G$. Since $G' = Q^T G Q$ and $G = (Q^{-1})^T G' Q^{-1}$ are the same relation, two forms on free modules of the same rank are isometric exactly when their Gram matrices are congruent, so the two classifications coincide.

**Proposition.** The isometry group is carried to the isometry group by an isometry: if $T : (M, B) \to (M', B')$ is an isometry, then $S \mapsto TST^{-1}$ is an isomorphism of groups $\operatorname{Isom}(M, B) \to \operatorname{Isom}(M', B')$.

**Proof.** From $B(Tu, Tv) = B(u, v)$ one gets $B(u, v) = B(T^{-1}u, T^{-1}v)$. For an isometry $S$ of $B$,

$$
B'(TST^{-1}u, TST^{-1}v) = B(ST^{-1}u, ST^{-1}v) = B(T^{-1}u, T^{-1}v) = B'(u, v),
$$

so $TST^{-1}$ is an isometry of $B'$; the assignment is a homomorphism with inverse $R \mapsto T^{-1}RT$. $\square$

The group is written $\operatorname{O}(M, B)$ when $B$ is symmetric, and $\operatorname{Sp}(M, B)$ when $B$ is alternating; the notation and the structure theory of these groups are developed .

### Congruence and the Discriminant

For a non-degenerate symmetric form on a free module, the determinant of the Gram matrix gives a congruence invariant modulo squares.

**Definition.** Let $B$ be a non-degenerate symmetric form on a free module of finite rank over a field $F$ of characteristic not $2$, with Gram matrix $G$. The **discriminant** of $B$ is the class

$$
\Delta(B) = \det G \in F^\times / (F^\times)^2,
$$

the image of $\det G$ in the group of square classes.

**Proposition.** The discriminant is well defined: a change of basis replaces $G$ by $P^T G P$ and multiplies the determinant by $(\det P)^2$, which is a square. If $B$ is replaced by $c\,B$ for $c \in F^\times$, then $\Delta(cB) = c^{n}\,\Delta(B)$, where $n$ is the rank.

**Proof.** Immediate from $\det(P^T G P) = (\det P)^2 \det G$ and from scaling $G$ by $c$. $\square$

The discriminant is the first congruence invariant of a non-degenerate symmetric form. It is not a complete invariant: over $\mathbb{R}$ the matrices $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(-1, -1)$ have the same discriminant $1$ but represent forms of opposite signature, treated.

## Summary

A **bilinear form** on an $R$-module $M$ is a function $B : M \times M \to R$ linear in each argument. It is **symmetric** if $B(u, v) = B(v, u)$, **skew-symmetric** if $B(u, v) = -B(v, u)$, and **alternating** if $B(v, v) = 0$ for all $v$. Every alternating form is skew-symmetric, and when $2$ is invertible the two notions coincide and a symmetric alternating form is zero.

On a free module of finite rank a form is represented by its **Gram matrix** $G_{ij} = B(e_i, e_j)$, with $B(u, v) = [u]^T G [v]$. Symmetry is $G = G^T$, skew-symmetry is $G = -G^T$, and a change of basis replaces $G$ by $P^T G P$; forms related in this way are **congruent**. The **rank** of $B$ is the rank of $G$.

The **radical** $\operatorname{rad}(B) = \{u : B(u, v) = 0 \ \forall v\}$ is the kernel of the map $M \to M^*$, $u \mapsto B(u, -)$. The form is **non-degenerate** when this map is an isomorphism; over a free module of finite rank this means $\det G$ is a unit of $R$. Over a field in finite dimension the conditions collapse: non-degeneracy, vanishing of the radical, invertibility of the Gram matrix, and $\operatorname{rank}(B) = \dim M$ are equivalent, and $\dim \operatorname{rad}(B) = \dim M - \operatorname{rank}(B)$. Over a general ring and in infinite dimension they do not: a form can have zero radical and still be degenerate.

The **orthogonal direct sum** $B_1 \perp B_2$ on $M_1 \oplus M_2$ is non-degenerate exactly when both summands are, and its Gram matrix is block diagonal. A non-degenerate alternating form has even rank, and over a field it has a **symplectic basis** $e_1, \ldots, e_m, f_1, \ldots, f_m$ with $B(e_i, f_j) = \delta_{ij}$; the case of rank two is the **symplectic plane**, which is not the quadratic hyperbolic plane. Isometries are the linear isomorphisms preserving $B$; they form the group $\operatorname{O}(M, B)$ for symmetric $B$ and $\operatorname{Sp}(M, B)$ for alternating $B$. The **discriminant** $\Delta(B) = \det G \in F^\times/(F^\times)^2$ is a congruence invariant of a non-degenerate symmetric form over a field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $F$, $K$ | Fields |
| $M$, $N$ | $R$-modules, left unless stated |
| $M^*$ | Dual module $\operatorname{Hom}_R(M, R)$ |
| $B$ | Bilinear form $B : M \times M \to R$ |
| $\operatorname{Bil}_R(M)$ | $R$-module of bilinear forms on $M$ |
| $G = (G_{ij})$ | Gram matrix, $G_{ij} = B(e_i, e_j)$ |
| $[v]$ | Coordinate column of $v$ in a basis |
| $P$ | Change-of-basis matrix |
| $u \perp v$ | $B(u, v) = 0$ |
| $S^\perp$ | Orthogonal complement of $S$ |
| $\operatorname{rad}(B)$ | Radical $\{u : B(u, v) = 0\ \forall v\}$ |
| $\operatorname{rank}(B)$ | Rank of the Gram matrix |
| $B_1 \perp B_2$ | Orthogonal direct sum of forms |
| $\operatorname{Isom}(M, B)$ | Isometry group of $B$ |
| $\operatorname{O}(M, B)$ | Orthogonal group of a symmetric form |
| $\operatorname{Sp}(M, B)$ | Symplectic group of an alternating form |
| $\delta_{ij}$ | Kronecker delta |
| $\Delta(B)$ | Discriminant $\det G \in F^\times/(F^\times)^2$ |





## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for the elementary theory of bilinear forms and their matrices.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for bilinear forms over rings and the dual-module formulation of non-degeneracy.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the congruence classification of symmetric and alternating forms.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the radical and the structure of isometry groups.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the alternating and symplectic cases over general rings.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for bilinear forms on modules over a commutative ring.
