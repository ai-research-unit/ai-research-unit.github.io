
# __The Unitary and Symplectic Groups__

## Introduction

The isometry group of a form depends on the type of the form. A symmetric bilinear form gives the orthogonal group, a Hermitian form gives the unitary group, and an alternating form gives the symplectic group. These three constructions, together with the general linear group and its determinant-one subgroup, produce the **classical groups**, and over the complex numbers their Lie algebras exhaust the four infinite families $A$, $B$, $C$, $D$ of the classification of simple Lie algebras.

This article develops the three constructions side by side, the standard matrix realisations $U(n)$, $SU(n)$ and $Sp(2n)$, the quaternionic analogue of the unitary group, and the four families with their dimensions and ranks. The base is a field $F$ or the field $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ when the analysis requires it. Symmetric and alternating forms, their radicals and non-degeneracy are from *Bilinear Forms*; the orthogonal group and its determinant are from *Isometries and Orthogonal Transformations* and *The Rotation Group and Orientation*. Hermitian forms are used here and developed; the trace and the reduced norm are cited from the same place. The exterior algebra and the Pfaffian are from *The Determinant and Alternating Forms*. The Lie algebras of these groups are related to *The Orthogonal Lie Algebra*.

## The Classical Groups from a Form

### The Common Pattern

The three families are instances of one construction. Let $V$ be a vector space over a field, let $\sigma$ be an involution of the field — the identity for the orthogonal and symplectic cases, complex conjugation for the unitary case — and let $h: V \times V \to F$ be a form that is $\sigma$-sesquilinear and Hermitian in the sense. The **isometry group** of $h$ is

$$
\operatorname{Isom}(V, h) = \{T \in GL(V) : h(Tu, Tv) = h(u, v) \text{ for all } u, v \in V\}.
$$

As in *Bilinear Forms*, these maps form a group, and the group depends only on the isometry class of $h$. Specialising the involution and the symmetry of $h$ recovers the three classical cases:

| Form | Involution $\sigma$ | Symmetry | Isometry group |
|---|---|---|---|
| symmetric bilinear $h$ | identity | $h(v, u) = h(u, v)$ | orthogonal $\operatorname{O}(V, h)$ |
| alternating bilinear $\omega$ | identity | $\omega(v, v) = 0$ | symplectic $\operatorname{Sp}(V, \omega)$ |
| Hermitian sesquilinear $h$ | conjugation | $h(v, u) = \sigma(h(u, v))$ | unitary $\operatorname{U}(V, h)$ |

The alternating case is written $\omega$ throughout, to keep it apart from the symmetric and the Hermitian forms $h$; its involution is the identity and its symmetry is the vanishing of $\omega(v, v)$ for every vector.

The general definition of a sesquilinear form relative to an involution, and the proof that the diagonal of a Hermitian form is a quadratic form over the fixed ring, lie outside this article; here we take the forms as given.

### Non-Degeneracy and the Special Groups

In each case the form is **non-degenerate** when the map $V \to V^*$, $v \mapsto h(v, -)$, is an isomorphism — a conjugate-linear one in the Hermitian case — and the isometry group is a subgroup of $GL(V)$. When the form is non-degenerate, taking determinants of the defining identity gives a constraint on $\det T$:

$$
\det(T)^2 = 1 \text{ for the orthogonal case}, \qquad |\det T| = 1 \text{ for the complex unitary case}, \qquad \det(T) = 1 \text{ for the symplectic case}.
$$

The **special** subgroups are the kernels of the determinant where the determinant is not already forced:

$$
\operatorname{SO}(V, h) = \operatorname{O}(V, h) \cap SL(V), \qquad \operatorname{SU}(V, h) = \operatorname{U}(V, h) \cap SL(V), \qquad \operatorname{Sp}(V, \omega) \subseteq SL(V).
$$

Thus the orthogonal and unitary groups meet the special linear group in their special subgroups, while the symplectic group is already contained in $SL(V)$. The last inclusion is proved below; it is the reason the symplectic family is labelled by a single symbol.

## The Unitary Group

### Hermitian Forms and the Definition

Let $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $V$ be a finite-dimensional $\mathbb{K}$-space. A **Hermitian form** on $V$ is a function $h : V \times V \to \mathbb{K}$ that is additive in each argument, satisfies

$$
h(\lambda u, \mu v) = \overline{\lambda}\, \mu\, h(u, v) \qquad (\lambda, \mu \in \mathbb{K}),
$$

and is Hermitian, $h(v, u) = \overline{h(u, v)}$. Over $\mathbb{R}$, where conjugation is the identity, this is a symmetric bilinear form; the interest is over $\mathbb{C}$. The **unitary group** of $h$ is

$$
\operatorname{U}(V, h) = \{T \in GL(V) : h(Tu, Tv) = h(u, v) \text{ for all } u, v\}.
$$

**Proposition.** If $h$ is non-degenerate, then $|\det T| = 1$ for every $T \in \operatorname{U}(V, h)$, and the determinant map $\operatorname{U}(V, h) \to \{z \in \mathbb{C} : |z| = 1\}$ has kernel $\operatorname{SU}(V, h)$.

**Proof.** Choose a basis and let $H$ be the matrix of $h$, so that $h(u, v) = u^{\dagger} H v$ with $u^{\dagger}$ the conjugate transpose. The isometry condition is $T^{\dagger} H T = H$. Taking determinants gives $\overline{\det T}\det T \det H = \det H$, so $|\det T|^2 = 1$ because $H$ is invertible. The kernel of the determinant is exactly $\operatorname{SU}(V, h)$. $\square$

### The Standard Unitary Groups

For $V = \mathbb{C}^n$ with the standard positive definite Hermitian form

$$
h(z, w) = \sum_{i=1}^{n} \overline{z_i}\, w_i,
$$

the matrix of $h$ is the identity, and the isometry condition becomes

$$
U^{\dagger} U = I, \qquad \text{equivalently} \qquad U^{-1} = U^{\dagger}.
$$

The group of such matrices is the **unitary group** $U(n)$, and its determinant-one subgroup is $SU(n)$. The columns of a unitary matrix form an orthonormal basis of $\mathbb{C}^n$, and the rows do too.

**Proposition.** $U(n)$ is a compact group of real dimension $n^2$, and $SU(n)$ is a compact connected group of real dimension $n^2 - 1$. The determinant map is surjective onto the circle, so

$$
U(n)/SU(n) \cong U(1) \cong S^1.
$$

**Proof.** The defining equation $U^{\dagger}U = I$ is a closed condition in $M_n(\mathbb{C})$, so $U(n)$ is closed; its columns are unit vectors, so it is bounded, hence compact. Near the identity it is a submanifold of the real vector space of $n \times n$ complex matrices, whose real dimension is $2n^2$. The condition $U^{\dagger}U = I$ is Hermitian, hence imposes $n^2$ real equations, and the derivative at $I$ is $A + A^{\dagger} = 0$, the anti-Hermitian condition, a real vector space of dimension $n^2$; the dimension of $U(n)$ near $I$ is therefore $2n^2 - n^2 = n^2$. The determinant has derivative the trace, which is nonzero on the anti-Hermitian matrices, so $SU(n)$ has dimension $n^2 - 1$. The determinant of a diagonal matrix $\operatorname{diag}(z, 1, \ldots, 1)$ with $|z| = 1$ realises every unit complex number, so the determinant is surjective onto $U(1)$. $\square$

**Example.** $U(1)$ is the circle group and $SU(1)$ is trivial. $SU(2)$ consists of the matrices $\begin{pmatrix} a & b \\ -\bar b & \bar a \end{pmatrix}$ with $|a|^2 + |b|^2 = 1$, a three-dimensional sphere; it is the unit quaternions, and it double covers $\operatorname{SO}(3)$, as described in the applications of the Clifford layer of this category, written in parallel.

### Relation to the Orthogonal Group

A Hermitian form on a complex space can be viewed as a real bilinear form on the underlying real space, and the unitary group is cut out by the real and imaginary parts.

**Proposition.** Let $h = s + i\,a$ with $s, a$ real-valued, $s$ symmetric bilinear and $a$ alternating bilinear. Then

$$
\operatorname{U}(V, h) = \operatorname{O}(V_{\mathbb{R}}, s) \cap \operatorname{Sp}(V_{\mathbb{R}}, a).
$$

**Proof.** The identity $h(Tu, Tv) = h(u, v)$ is equivalent to the pair of real identities $s(Tu, Tv) = s(u, v)$ and $a(Tu, Tv) = a(u, v)$, because the real and imaginary parts of a complex number vanish together. The first is the orthogonal condition for $s$ and the second the symplectic condition for $a$. $\square$

This is the precise sense in which the unitary group lies between the orthogonal and symplectic groups: it is the intersection of one of each on the realification of the space.

## Hermitian Forms and Inertia

### The Gram Matrix of a Hermitian Form

Let $h$ be a Hermitian form on a finite-dimensional $\mathbb{C}$-space $V$, in the sense. In a basis $e_1, \ldots, e_n$ the Gram matrix $H$ with $H_{ij} = h(e_i, e_j)$ satisfies $H^{\dagger} = H$, and

$$
h(u, v) = u^{\dagger} H v .
$$

For $u = v$ the number $u^{\dagger}Hu$ is real, because its conjugate is $u^{\dagger}H^{\dagger}u = u^{\dagger}Hu$; so the diagonal $v \mapsto h(v, v)$ is a real-valued function even though $h$ is not symmetric. A change of basis with matrix $P$ replaces $H$ by the Hermitian-congruent matrix $P^{\dagger}HP$.

**Theorem (inertia for Hermitian forms).** Let $h$ be a Hermitian form on a finite-dimensional $\mathbb{C}$-space of dimension $n$. Then there are unique integers $p, r, z \geq 0$ with $p + r + z = n$ and a basis in which the Gram matrix is $\operatorname{diag}(I_p, -I_r, 0_z)$.

**Proof.** The argument is that of Sylvester's law of inertia for real quadratic forms: the diagonalisation by completing the square applies, because the diagonal entries $h(e_i, e_i)$ are real and the substitution $v \mapsto v - \frac{h(e, v)}{h(e,e)}e$ kills the entries $h(v, e)$ for a vector with $h(e,e) \neq 0$; the uniqueness follows by counting the maximal dimension $p$ of a subspace on which $h$ is positive definite and the maximal dimension $r$ on which it is negative definite, both of which are invariants of $h$. $\square$

The triple $(p, r, z)$ is the **signature** of $h$, and $h$ is non-degenerate exactly when $z = 0$. The isometry group of the form $\operatorname{diag}(I_p, -I_r)$ is written

$$
U(p, r) = \{M \in GL(n, \mathbb{C}) : M^{\dagger} \begin{pmatrix} I_p & 0 \\ 0 & -I_r\end{pmatrix} M = \begin{pmatrix} I_p & 0 \\ 0 & -I_r\end{pmatrix}\},
$$

with special subgroup $SU(p, r)$ the kernel of the determinant; both have real dimension $n^2$ and $n^2 - 1$ respectively, since the counting of the compact case uses only the Hermitian condition on $M^{\dagger}HM = H$ and the dimension of $H$ as a real vector space. For $p = n$ the group is the compact $U(n)$ of the previous section, and for $p, r > 0$ it is non-compact.

### The Group $U(1, 1)$

The smallest non-compact case is $h(z, w) = \bar z_1 w_1 - \bar z_2 w_2$ on $\mathbb{C}^2$. Writing a matrix as $T = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$, the condition $T^{\dagger}\operatorname{diag}(1,-1)T = \operatorname{diag}(1,-1)$ is the three equations

$$
|a|^2 - |c|^2 = 1, \qquad |d|^2 - |b|^2 = 1, \qquad \bar a b - \bar c d = 0 .
$$

**Example.** The matrices $\begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t\end{pmatrix}$ for $t \in \mathbb{R}$ and $\begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta}\end{pmatrix}$ for $\theta \in \mathbb{R}$ both lie in $SU(1,1)$: for the first the three equations reduce to $\cosh^2 t - \sinh^2 t = 1$, and for the second $|e^{i\theta}|^2 = 1$. The first family is a hyperbolic one-parameter subgroup, the second a compact circle, and the two generate a subgroup of $SU(1,1)$ through which the two types of one-parameter subgroup of a non-compact real form are visible.

**Remark.** The group $SU(1,1)$ is isomorphic to $SL(2, \mathbb{R})$ and to $Sp(2, \mathbb{R})$, the three real forms of $\mathfrak{sl}(2, \mathbb{C})$ of rank one; the compact form $SU(2)$ is not isomorphic to them. The isomorphism $SU(1,1) \cong Sp(2, \mathbb{R})$ is the first case of the general statement that the quaternionic and the symplectic descriptions agree over $\mathbb{C}$.

## The Symplectic Group

### Alternating Forms

Let $V$ be a finite-dimensional space over a field $F$ of characteristic not $2$, with a non-degenerate alternating form $\omega$. By *Bilinear Forms*, $\dim V = 2m$ is even and there is a symplectic basis $e_1, \ldots, e_m, f_1, \ldots, f_m$ with $\omega(e_i, f_j) = \delta_{ij}$. The **symplectic group** of $\omega$ is

$$
\operatorname{Sp}(V, \omega) = \{T \in GL(V) : \omega(Tu, Tv) = \omega(u, v) \text{ for all } u, v\}.
$$

### The Standard Symplectic Group

For $V = F^{2m}$ with the standard alternating form given by the block matrix

$$
\Omega = \begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}, \qquad \omega(x, y) = x^T \Omega\, y,
$$

the isometry condition is $M^T \Omega M = \Omega$, and the group of such matrices is written $Sp(2m, F)$ or $Sp(2m)$ over a field understood. The entries of a symplectic matrix satisfy the quadratic relations encoded in $M^T \Omega M = \Omega$.

**Theorem.** Every symplectic matrix has determinant $1$. Hence

$$
\operatorname{Sp}(2m, F) \subseteq SL(2m, F).
$$

**Proof.** Let $\operatorname{Pf}$ be the Pfaffian, which satisfies $\operatorname{Pf}(M^T \Omega M) = \det(M)\operatorname{Pf}(\Omega)$ for every $2m \times 2m$ matrix $M$, and $\operatorname{Pf}(\Omega) = (-1)^{m(m-1)/2} \neq 0$ for the matrix above. If $M^T \Omega M = \Omega$, applying $\operatorname{Pf}$ gives $\det(M)\operatorname{Pf}(\Omega) = \operatorname{Pf}(\Omega)$, that is $\det M = 1$. $\square$

**Proposition.** $Sp(2m, F)$ has dimension $2m^2 + m$ over $F$; over $\mathbb{R}$ or $\mathbb{C}$ it is connected, and it is non-compact.

**Proof.** The equations $M^T \Omega M = \Omega$ are $\binom{2m}{2}$ scalar conditions on the $4m^2$ entries of $M$ (the antisymmetric part of $M^T\Omega M$, since the symmetric part is automatic). Hence the dimension is at most $4m^2 - m(2m-1) = 2m^2 + m$; equality holds because the derivative at the identity imposes the same count. The connectedness and non-compactness are standard. $\square$

The plane case is the base of the family and can be settled directly.

**Proposition.** $\operatorname{Sp}(2, F) = SL(2, F)$.

**Proof.** Let $M = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$ and let $\Omega = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$. Then

$$
M^{T}\Omega M = \begin{pmatrix} 0 & ad - bc \\ bc - ad & 0\end{pmatrix} = (\det M)\,\Omega,
$$

so $M^{T}\Omega M = \Omega$ if and only if $\det M = 1$, since $\Omega \neq 0$. $\square$

So the symplectic family begins with the special linear group in dimension two, and $Sp(2, F) \cong SL(2, F)$: the alternating form on a plane is unique up to scale, and every determinant-one $2 \times 2$ matrix preserves it.

### The Compact Form inside the Split Form

The intersection of the symplectic and orthogonal groups on a real space of even dimension is the unitary group, and this identifies the compact real form inside the split one.

**Theorem.** With the standard alternating form and the standard positive definite form on $\mathbb{R}^{2m}$,

$$
Sp(2m, \mathbb{R}) \cap O(2m) = U(m).
$$

**Proof.** Let $A \in GL(2m, \mathbb{R})$ satisfy $A^{T}\Omega A = \Omega$ and $A^{T}A = I$. From the first relation, $\Omega A = (A^{T})^{-1}\Omega = A\Omega$, because $A^{T} = A^{-1}$ by the second; so $A$ commutes with $\Omega$. Identifying $\mathbb{R}^{2m}$ with $\mathbb{C}^m$ by taking $\Omega$ as the matrix of multiplication by $i$, commutativity with $\Omega$ says exactly that $A$ is complex-linear, and the orthogonal condition $A^{T}A = I$ says that $A$ preserves the Euclidean form, which is the real part of the standard Hermitian form. Hence $A$ is complex-linear and unitary, that is $A \in U(m)$. Conversely, let $U \in U(m)$ and write it as the real matrix $A = \begin{pmatrix} X & -Y \\ Y & X\end{pmatrix}$; the conditions $X^{T}X + Y^{T}Y = I$ and $X^{T}Y - Y^{T}X = 0$, which are $U^{\dagger}U = I$, give $A^{T}A = I$ directly, and $A$ commutes with $\Omega$ because it is complex-linear, so $A^{T}\Omega A = A^{-1}\Omega A = \Omega$. $\square$

Both groups in the statement are compact, and the theorem exhibits $U(m)$ as a maximal compact subgroup of the non-compact group $Sp(2m, \mathbb{R})$. The dimension count reflects the splitting: $\dim Sp(2m, \mathbb{R}) = 2m^2 + m$ and $\dim U(m) = m^2$, the difference $m^2 + m$ being the dimension of the symmetric space $Sp(2m, \mathbb{R})/U(m)$.

## The Quaternionic Case

### Quaternionic Hermitian Forms

Let $D$ be a division ring with an involution $\sigma$, for instance the quaternions $\mathbb{H}$ with conjugation. A **$\sigma$-Hermitian form** on a right $D$-module $V$ is additive in each argument with

$$
h(xa, yb) = \sigma(a)\,h(x, y)\,b, \qquad h(y, x) = \sigma(h(x, y)),
$$

. Its isometry group is the **unitary group** $\operatorname{U}(V, h)$ of the Hermitian form. For $D = \mathbb{H}$ and the standard form $h(x, y) = \sum_i \bar{x}_i y_i$ on $\mathbb{H}^n$, the resulting group is the **compact symplectic group** $Sp(n)$, also written $U(n, \mathbb{H})$.

**Warning on notation.** The symbol $Sp$ carries two meanings: $Sp(2m, F)$ is the isometry group of an alternating form over a field, a non-compact group, while $Sp(n)$ is the isometry group of a quaternionic Hermitian form, a compact group. The two agree only through the identification of $Sp(n)$ with the compact real form of $Sp(2n, \mathbb{C})$: the complexification of the quaternionic unitary group is the symplectic group $Sp(2n, \mathbb{C})$.

**Proposition.** $Sp(n)$ is a compact connected group of real dimension $n(2n + 1)$. It is the intersection $Sp(2n, \mathbb{C}) \cap U(2n)$ inside $GL(2n, \mathbb{C})$.

**Proof.** A quaternionic $n \times n$ matrix has $4n^2$ real parameters; the condition $A^{\dagger}A = I$ imposes $n(2n-1)$ independent real equations, leaving dimension $4n^2 - n(2n-1) = n(2n+1)$. Compactness is the closedness and boundedness of the defining condition, as in the complex case. The identification of $Sp(n)$ with $Sp(2n, \mathbb{C}) \cap U(2n)$ is the standard realisation of the quaternions as $2 \times 2$ complex matrices. $\square$

### Relation to $GL$ and $SL$

The classical groups fit into the chain

$$
SU(n) \subset U(n) \subset GL(n, \mathbb{C}), \qquad Sp(2m, F) \subset SL(2m, F) \subset GL(2m, F),
$$

and $SO(n) \subset O(n) \subset GL(n, \mathbb{R})$. The special linear group is the kernel of the determinant in each ambient general linear group, and the special orthogonal and special unitary groups are the intersections of their groups with $SL$, while the symplectic group is contained in $SL$ by the Pfaffian theorem above.

## The Four Families

### The Classification

Over an algebraically closed field the simple Lie algebras fall into the four infinite families $A$, $B$, $C$, $D$ and the five exceptional algebras; the classical groups produce exactly the four families.

| Family | Group over $\mathbb{C}$ | Rank | Dimension |
|---|---|---|---|
| $A_n$ | $SL(n+1, \mathbb{C})$ | $n$ | $n(n+2)$ |
| $B_n$ | $SO(2n+1, \mathbb{C})$ | $n$ | $n(2n+1)$ |
| $C_n$ | $Sp(2n, \mathbb{C})$ | $n$ | $n(2n+1)$ |
| $D_n$ | $SO(2n, \mathbb{C})$ | $n$ | $n(2n-1)$ |

The families $B_n$ and $C_n$ have the same dimension and rank and are dual to one another; the Lie algebras $\mathfrak{so}(2n+1)$ and $\mathfrak{sp}(2n)$ are not isomorphic, but their root systems are dual, with the long and short roots interchanged. The orthogonal family splits into $B$ and $D$ because $\operatorname{SO}(2n+1)$ and $\operatorname{SO}(2n)$ have different root systems: $B_n$ has roots of two lengths, while $D_n$ is simply laced for $n \geq 3$.

**Example.** $A_1 = B_1 = C_1$ is the case of rank one: $SL(2)$, $SO(3)$, and $Sp(2)$ all have the same Lie algebra $\mathfrak{sl}(2)$, and the three descriptions are related by the low-dimensional coincidences of *The Orthogonal Lie Algebra*. $D_2 = A_1 \times A_1$ is the rank-two exception $\mathfrak{so}(4) \cong \mathfrak{sl}(2) \oplus \mathfrak{sl}(2)$, which is not simple; the family $D_n$ is simple for $n \geq 3$.

### Real Forms and Compact Groups

Each complex family has several real forms. The **compact** real forms are $SU(n)$ for $A_n$, $SO(2n+1)$ for $B_n$, $Sp(n)$ for $C_n$, and $SO(2n)$ for $D_n$. The **split** real forms are $SL(n+1, \mathbb{R})$, $SO(n, n+1)$, $Sp(2n, \mathbb{R})$, and $SO(n, n)$. The isometry groups of the real forms of a quadratic form are the groups $\operatorname{O}(p, r)$ of *The Rotation Group and Orientation*, and the isometry groups of the real forms of a Hermitian form are the groups $U(p, r)$; the corresponding Lie algebras are the real forms of *The Orthogonal Lie Algebra*.

**Remark.** The unitary and symplectic matrix groups belong to the classical groups as studied in category 04; the role of this article is to exhibit them as the isometry groups of the three types of form, so that the form, not the matrix, is the primary datum.

## Summary

The **classical groups** are the isometry groups of the three types of form. A non-degenerate **symmetric bilinear** form gives the **orthogonal group** $\operatorname{O}(V, h)$ with special subgroup $\operatorname{SO}(V, h) = \operatorname{O}(V, h) \cap SL(V)$; a non-degenerate **alternating** form gives the **symplectic group** $\operatorname{Sp}(V, \omega)$; and a non-degenerate **Hermitian** form gives the **unitary group** $\operatorname{U}(V, h)$ with special subgroup $\operatorname{SU}(V, h) = \operatorname{U}(V, h) \cap SL(V)$.

Over $\mathbb{C}$ the standard unitary groups are $U(n) = \{U : U^{\dagger}U = I\}$ and $SU(n)$, of real dimensions $n^2$ and $n^2 - 1$; $U(n)$ is compact and $U(n)/SU(n) \cong S^1$. A Hermitian form $h = s + ia$ has unitary group $\operatorname{O}(V_{\mathbb{R}}, s) \cap \operatorname{Sp}(V_{\mathbb{R}}, a)$, the intersection of an orthogonal and a symplectic group on the realification.

The standard symplectic group $Sp(2m, F) = \{M : M^T\Omega M = \Omega\}$ has dimension $2m^2 + m$, is contained in $SL(2m, F)$ (every symplectic matrix has determinant $1$, by the Pfaffian), is connected and non-compact, and in dimension two coincides with $SL(2, F)$. The **quaternionic unitary group** $Sp(n)$, of dimension $n(2n+1)$, is compact and is the compact real form of $Sp(2n, \mathbb{C})$; the notation $Sp$ therefore carries two distinct meanings, which the context separates.

Over an algebraically closed field the simple Lie algebras coming from these groups are the four families $A_n = \mathfrak{sl}(n+1)$, $B_n = \mathfrak{so}(2n+1)$, $C_n = \mathfrak{sp}(2n)$ and $D_n = \mathfrak{so}(2n)$, of ranks $n$ and dimensions $n(n+2)$, $n(2n+1)$, $n(2n+1)$ and $n(2n-1)$. $B$ and $C$ are dual families of equal dimension; $D_2$ is not simple, splitting as $A_1 \times A_1$. The compact real forms are $SU(n)$, $SO(2n+1)$, $Sp(n)$, $SO(2n)$, and the split real forms are $SL(n+1, \mathbb{R})$, $SO(n, n+1)$, $Sp(2n, \mathbb{R})$, $SO(n, n)$.

A **Hermitian form** has a Hermitian Gram matrix $H = H^{\dagger}$ and a real-valued diagonal $v \mapsto h(v, v)$. By the **inertia theorem for Hermitian forms** it has a unique signature $(p, r, z)$ with normal form $\operatorname{diag}(I_p, -I_r, 0_z)$, and its isometry group is $U(p, r)$, of real dimension $n^2$, with special subgroup $SU(p, r)$ of dimension $n^2 - 1$. The case $U(1, 1)$ is non-compact and contains both a hyperbolic and a compact one-parameter subgroup; $SU(1, 1) \cong SL(2, \mathbb{R}) \cong Sp(2, \mathbb{R})$.

The compact and split forms of the symplectic family meet in the unitary group: on $\mathbb{R}^{2m}$ with the standard alternating and Euclidean forms, $Sp(2m, \mathbb{R}) \cap O(2m) = U(m)$, because a real matrix that is both symplectic and orthogonal commutes with $\Omega$ and is therefore complex-linear. Hence $U(m)$ is a maximal compact subgroup of $Sp(2m, \mathbb{R})$, of dimension $m^2$ inside the ambient dimension $2m^2 + m$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field |
| $\mathbb{K}$ | Either $\mathbb{R}$ or $\mathbb{C}$ |
| $V$ | Finite-dimensional space over $F$ or $\mathbb{K}$ |
| $h$, $s$, $a$ | Form; its symmetric part; its alternating part |
| $\sigma$ | Involution of the base ring used in sesquilinearity |
| $\overline{\cdot}$, ${}^{\dagger}$ | Complex conjugation of coefficients; conjugate transpose (Hermitian conjugation) |
| $\operatorname{U}(V, h)$ | Unitary group of a Hermitian form |
| $\operatorname{SU}(V, h)$, $SU(n)$ | Special unitary group, determinant one |
| $U(n)$ | Standard unitary group, $U^{\dagger}U = I$ |
| $H$ | Hermitian Gram matrix, $H^{\dagger} = H$, $h(u,v) = u^{\dagger}Hv$ |
| $U(p, r)$, $SU(p, r)$ | Unitary group of a Hermitian form of signature $(p, r)$, and its determinant-one subgroup |
| $p, r, z$ | Signature of a Hermitian form, $p + r + z = n$ |
| $I_p$ | Identity matrix of size $p$ |
| $\operatorname{diag}$ | Diagonal matrix with the displayed entries |
| $\operatorname{Sp}(V, \omega)$ | Symplectic group of an alternating form |
| $Sp(2m, F)$ | Standard symplectic group, $M^T\Omega M = \Omega$ |
| $Sp(n)$ | Compact quaternionic unitary group (a clash of notation with the previous line, separated by context) |
| $\Omega$ | Standard alternating matrix $\begin{pmatrix} 0 & I \\ -I & 0\end{pmatrix}$ |
| $\omega$ | Alternating form, $\omega(x, y) = x^T\Omega y$ |
| $\operatorname{Pf}$ | Pfaffian |
| $\delta_{ij}$ | Kronecker delta |
| $GL(V)$, $SL(V)$ | General and special linear groups |
| $A_n, B_n, C_n, D_n$ | The four classical families of simple Lie algebras |
| $\mathfrak{sl}, \mathfrak{so}, \mathfrak{sp}$ | The corresponding Lie algebras |
| $\mathbb{H}$ | Quaternions |
| $\mathbb{C}, \mathbb{R}$ | Complex and real numbers |





## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the classical groups over general rings and their isometry-theoretic definition.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for the unitary, symplectic and orthogonal groups and their interrelations.
- Roger Howe, "Remarks on classical invariant theory", *Transactions of the American Mathematical Society* 313 (1989), 539–570, for the form-first viewpoint on the classical groups.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6* (Springer, 2002), for the root systems and the classification of the classical families.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the four families and their real forms.
