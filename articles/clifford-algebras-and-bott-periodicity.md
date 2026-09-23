# __Clifford Algebras and Bott Periodicity__

## Introduction

This article explains the periodic structure of the classification of Clifford algebras. It continues the account begun in *Clifford Algebras* and developed in *Clifford Algebras in Finite Dimensions* and *Clifford Algebras in Finite Dimensions categorization*. The treatment is introductory and purely mathematical.

The preceding articles compute the Clifford algebra $\operatorname{Cl}(M, Q)$ of a free module of finite rank with a non-degenerate quadratic form, and work out the low-dimensional cases over the fields $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ and over the ring $\mathbb{D}$ of split complex numbers. The present article explains why those tables have the shape they do. The classification is periodic. Over the real numbers the period is eight; over the complex numbers it is two. The periodicity is not an artefact of the low-dimensional computations: it follows from the tensor product decomposition together with the single computation $\operatorname{Cl}_{8,0}(\mathbb{R}) \cong M_{16}(\mathbb{R})$.

We assume familiarity with the general definition, the universal property, the fundamental relation, the tensor product decomposition, the volume element, the even subalgebra, and the low-dimensional classification. All of these are treated in the preceding articles.

We use the sign convention of the series,
$$
v^2 = Q(v) \cdot 1,
$$
and we take the quadratic form to be non-degenerate. Over $\mathbb{R}$ we write $\operatorname{Cl}_{p,q}(\mathbb{R})$ for the Clifford algebra of a form with $p$ positive and $q$ negative squares, and we abbreviate
$$
\operatorname{Cl}_n = \operatorname{Cl}_{n,0}(\mathbb{R}).
$$
The complex Clifford algebra of rank $n$ is written $\mathbb{C}l_n$. The ordinary tensor product is written $\otimes$ and the graded tensor product is written $\hat{\otimes}$; in the graded tensor product, odd elements of the two factors anticommute.

**A caution about conventions.** Both signs $v^2 = \pm Q(v)$ occur in the literature, and the low-dimensional tables differ between them. Every table below is stated in the convention $v^2 = Q(v)$. The periodicity isomorphisms themselves are insensitive to the choice, because the other convention replaces $Q$ by $-Q$ and so interchanges $p$ and $q$.

---

# Part I: The Periodicity Isomorphisms

## 1. The real periodicity

**Theorem (real periodicity).** For every $n \geq 0$ there is an isomorphism of real algebras
$$
\operatorname{Cl}_{n+8,0}(\mathbb{R}) \cong \operatorname{Cl}_{n,0}(\mathbb{R}) \otimes_\mathbb{R} M_{16}(\mathbb{R}).
$$
More generally, for all $p, q \geq 0$,
$$
\operatorname{Cl}_{p+8,q}(\mathbb{R}) \cong \operatorname{Cl}_{p,q}(\mathbb{R}) \otimes_\mathbb{R} M_{16}(\mathbb{R}),
$$
$$
\operatorname{Cl}_{p,q+8}(\mathbb{R}) \cong \operatorname{Cl}_{p,q}(\mathbb{R}) \otimes_\mathbb{R} M_{16}(\mathbb{R}).
$$

The shift is $8$ and the matrix size is $16 = 2^4$. Both numbers are forced. The dimension of $M_{16}(\mathbb{R})$ is $256 = 2^8$, exactly the factor by which the dimension of a Clifford algebra grows when the rank grows by $8$; and $16$ is the dimension of the irreducible module of $\operatorname{Cl}_8$, which is the minimal period.

The base case is
$$
\operatorname{Cl}_{8,0}(\mathbb{R}) \cong M_{16}(\mathbb{R}), \qquad \operatorname{Cl}_{0,8}(\mathbb{R}) \cong M_{16}(\mathbb{R}).
$$
Two remarks. First, $\operatorname{Cl}_{8,0}$ and $\operatorname{Cl}_{0,8}$ are isomorphic to each other although their quadratic forms have opposite signs; the isomorphism is not the identity on generators. Second, both are full matrix algebras and therefore split, with trivial Brauer class. This is the algebraic content of the statement that the period is $8$.

## 2. The complex periodicity

**Theorem (complex periodicity).** For every $n \geq 0$ there is an isomorphism of complex algebras
$$
\mathbb{C}l_{n+2} \cong \mathbb{C}l_n \otimes_\mathbb{C} M_2(\mathbb{C}).
$$
The shift is $2$ and the matrix size is $2$, and the base case is
$$
\mathbb{C}l_2 \cong M_2(\mathbb{C}).
$$

So the complex period is $2$, not $8$. Complexifying the real statement does not give a period-$8$ statement over $\mathbb{C}$: since $M_{16}(\mathbb{R}) \otimes_\mathbb{R} \mathbb{C} \cong M_{16}(\mathbb{C})$ and $M_{16}(\mathbb{C}) \cong M_2(\mathbb{C})^{\otimes 4}$, four complex periods make one real period. Section 8 makes the relation between the two statements precise.

## 3. The tensor product decomposition as the source

The periodicity is a formal consequence of the tensor product decomposition of the preceding article. For an orthogonal direct sum,
$$
\operatorname{Cl}(M_1 \oplus M_2, Q_1 \oplus Q_2) \cong \operatorname{Cl}(M_1, Q_1) \hat{\otimes} \operatorname{Cl}(M_2, Q_2).
$$
In particular, for definite real forms,
$$
\operatorname{Cl}_{n+k,0}(\mathbb{R}) \cong \operatorname{Cl}_{n,0}(\mathbb{R}) \hat{\otimes} \operatorname{Cl}_{k,0}(\mathbb{R}).
$$
Taking $k = 8$ and using $\operatorname{Cl}_{8,0} \cong M_{16}(\mathbb{R})$ gives the real periodicity. Similarly,
$$
\mathbb{C}l_{n+2} \cong \mathbb{C}l_n \hat{\otimes} \mathbb{C}l_2
$$
together with $\mathbb{C}l_2 \cong M_2(\mathbb{C})$ gives the complex periodicity.

The reason a matrix algebra produces periodicity rather than unbounded growth is the simplest case of Morita's theorem: $M_k(F)$ is Morita equivalent to $F$. Tensoring by $M_{16}(\mathbb{R})$ changes the algebra but not its category of modules, up to an equivalence. The module theory of $\operatorname{Cl}_{n+8}$ is therefore the module theory of $\operatorname{Cl}_n$, and the type of the Clifford algebra repeats. Section 11 develops this point.

## 4. One-step recursions and the rank-one cases

It is useful to record the recursions that add a single generator or a single pair of generators:
$$
\operatorname{Cl}_{p+1,q+1} \cong \operatorname{Cl}_{p,q} \otimes_\mathbb{R} M_2(\mathbb{R}), \qquad \mathbb{C}l_{n+1} \cong \mathbb{C}l_n \hat{\otimes} \mathbb{C}l_1.
$$
The rank-one algebras are
$$
\operatorname{Cl}_{1,0} \cong \mathbb{R} \oplus \mathbb{R}, \qquad \operatorname{Cl}_{0,1} \cong \mathbb{C}, \qquad \mathbb{C}l_1 \cong \mathbb{C} \oplus \mathbb{C}.
$$
These recursions are the engine of the classification: starting from $\operatorname{Cl}_{0,0} \cong \mathbb{R}$ and applying them repeatedly produces the tables of Part II. The periodicity is what the recursion produces after eight steps, when the accumulated matrix factor has become invisible to the module category.

## 5. The volume element

Let $e_1, \ldots, e_n$ be an orthogonal basis, so that $B(e_i, e_j) = 0$ for $i \neq j$ and the generators anticommute. The **volume element** is
$$
\omega = e_1 e_2 \cdots e_n.
$$
Its square is the scalar
$$
\omega^2 = (-1)^{n(n-1)/2}\, Q(e_1) Q(e_2) \cdots Q(e_n) \cdot 1.
$$
For the standard forms used here it therefore takes the values $\pm 1$. For $\operatorname{Cl}_{n,0}$, and for $\mathbb{C}l_n$ after rescaling the generators to $Q(e_i) = +1$,
$$
\omega^2 = (-1)^{n(n-1)/2},
$$
which is $+1$ for $n \equiv 0, 1, 4, 5 \pmod 8$ and $-1$ for $n \equiv 2, 3, 6, 7 \pmod 8$. For $\operatorname{Cl}_{0,n}$, where $Q(e_i) = -1$,
$$
\omega^2 = (-1)^{n(n+1)/2},
$$
which is $+1$ for $n \equiv 0, 3, 4, 7 \pmod 8$ and $-1$ for $n \equiv 1, 2, 5, 6 \pmod 8$. The sign of $\omega^2$ is one of the data that distinguish the eight residues.

The volume element plays two roles. When $n$ is odd, $\omega$ is central, and the centre of the Clifford algebra is two-dimensional, spanned by $1$ and $\omega$. The algebra is a product of two simple algebras when $\omega^2 = +1$, and a central simple algebra over $\mathbb{C}$ when $\omega^2 = -1$. When $n$ is even, $\omega$ is not central, but it commutes with the even subalgebra and anticommutes with the odd part; it is then the **chirality operator**. Its eigenspaces in the spinor module are the half-spinor modules, and the sign of $\omega^2$ is part of the data that decide whether those modules are real, complex or quaternionic. Section 15 takes this up.

## 6. Explicit generators and the periodicity map

For $\mathbb{C}l_8$ the isomorphism $\mathbb{C}l_8 \cong M_{16}(\mathbb{C})$ can be exhibited explicitly. Let
$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$
be the Pauli matrices, so that $\sigma_j^2 = I$ and $\sigma_j \sigma_k = -\sigma_k \sigma_j$ for $j \neq k$. On
$$
\mathbb{C}^{16} = (\mathbb{C}^2)^{\otimes 4}
$$
define, for $k = 1, 2, 3, 4$,
$$
\gamma_{2k-1} = \sigma_3^{\otimes (k-1)} \otimes \sigma_1 \otimes I^{\otimes (4-k)}, \qquad
\gamma_{2k} = \sigma_3^{\otimes (k-1)} \otimes \sigma_2 \otimes I^{\otimes (4-k)}.
$$
The eight matrices $\gamma_1, \ldots, \gamma_8$ are pairwise anticommuting, and each squares to $I$. They therefore generate a Clifford algebra of dimension $2^8 = 256 = 16^2$ on a space of dimension $16$, that is, the full matrix algebra $M_{16}(\mathbb{C})$, so that $\mathbb{C}l_8 \cong M_{16}(\mathbb{C})$. For the real forms the classical computation gives the base case of the real periodicity,
$$
\operatorname{Cl}_{8,0}(\mathbb{R}) \cong M_{16}(\mathbb{R}), \qquad \operatorname{Cl}_{0,8}(\mathbb{R}) \cong M_{16}(\mathbb{R}),
$$
the complex representation above being the complexification of a real one.

At the level of modules the periodicity reads as follows. If $S_n$ is an irreducible $\operatorname{Cl}_n$-module and $\Delta_8$ is an irreducible $\operatorname{Cl}_8$-module, of dimension $16$, then
$$
S_n \otimes \Delta_8
$$
is an irreducible $\operatorname{Cl}_{n+8}$-module. This is the periodicity map on modules, and it is the content of Section 14.

---

# Part II: The Classification

## 7. The real classification

Up to isomorphism, $\operatorname{Cl}_{p,q}(\mathbb{R})$ depends only on the rank $n = p + q$ and on the difference $p - q$, modulo $8$. The two definite families are as follows.

| $n$ | $\operatorname{Cl}_{n,0}(\mathbb{R})$ | $\operatorname{Cl}_{0,n}(\mathbb{R})$ |
|---|---|---|
| 0 | $\mathbb{R}$ | $\mathbb{R}$ |
| 1 | $\mathbb{R} \oplus \mathbb{R}$ | $\mathbb{C}$ |
| 2 | $M_2(\mathbb{R})$ | $\mathbb{H}$ |
| 3 | $M_2(\mathbb{C})$ | $\mathbb{H} \oplus \mathbb{H}$ |
| 4 | $M_2(\mathbb{H})$ | $M_2(\mathbb{H})$ |
| 5 | $M_2(\mathbb{H}) \oplus M_2(\mathbb{H})$ | $M_4(\mathbb{C})$ |
| 6 | $M_4(\mathbb{H})$ | $M_8(\mathbb{R})$ |
| 7 | $M_8(\mathbb{C})$ | $M_8(\mathbb{R}) \oplus M_8(\mathbb{R})$ |
| 8 | $M_{16}(\mathbb{R})$ | $M_{16}(\mathbb{R})$ |

The table continues with period $8$: each entry for $n + 8$ is the entry for $n$ tensored with $M_{16}(\mathbb{R})$. The low-dimensional cases of the preceding articles are recovered as the rows with $n \leq 4$, together with the general-signature cases recorded there, such as $\operatorname{Cl}_{2,1} \cong M_2(\mathbb{R}) \oplus M_2(\mathbb{R})$ and $\operatorname{Cl}_{1,3} \cong M_2(\mathbb{H})$.

## 8. The complex classification and complexification

Over $\mathbb{C}$ there is a single non-degenerate quadratic form in each rank, and the classification is
$$
\mathbb{C}l_{2k} \cong M_{2^k}(\mathbb{C}), \qquad \mathbb{C}l_{2k+1} \cong M_{2^k}(\mathbb{C}) \oplus M_{2^k}(\mathbb{C}).
$$
The first few cases are:

| $n$ | $\mathbb{C}l_n$ |
|---|---|
| 0 | $\mathbb{C}$ |
| 1 | $\mathbb{C} \oplus \mathbb{C}$ |
| 2 | $M_2(\mathbb{C})$ |
| 3 | $M_2(\mathbb{C}) \oplus M_2(\mathbb{C})$ |
| 4 | $M_4(\mathbb{C})$ |
| 5 | $M_4(\mathbb{C}) \oplus M_4(\mathbb{C})$ |
| 6 | $M_8(\mathbb{C})$ |
| 7 | $M_8(\mathbb{C}) \oplus M_8(\mathbb{C})$ |

Complexification forgets the signature: for every real form of rank $n$,
$$
\operatorname{Cl}_{p,q}(\mathbb{R}) \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C}l_{p+q},
$$
and in particular $\operatorname{Cl}_{n,0} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C}l_n$. The complex classification is thus the common collapse of the two definite real families. The arithmetic of the two periods is $8 = 4 \cdot 2$: one real period is four complex periods.

## 9. The even subalgebra

The even subalgebra satisfies
$$
\operatorname{Cl}^0_{p,q} \cong \operatorname{Cl}_{q,p-1} \quad (p \geq 1), \qquad \operatorname{Cl}^0_{0,q} \cong \operatorname{Cl}_{0,q-1}.
$$
For the two definite families both formulae reduce to the same statement:
$$
\operatorname{Cl}^0_{n,0}(\mathbb{R}) \cong \operatorname{Cl}_{0,n-1}(\mathbb{R}), \qquad \operatorname{Cl}^0_{0,n}(\mathbb{R}) \cong \operatorname{Cl}_{0,n-1}(\mathbb{R}),
$$
for $n \geq 1$. So the even subalgebra of either definite algebra of rank $n$ is the negative-definite algebra of rank $n-1$. Complexly,
$$
\mathbb{C}l_n^0 \cong \mathbb{C}l_{n-1}
$$
for $n \geq 1$. For example, $\mathbb{C}l_2^0$ is spanned by $1$ and $e_1 e_2$, and $(e_1 e_2)^2 = -1$, so $\mathbb{C}l_2^0 \cong \mathbb{C}[x]/(x^2+1) \cong \mathbb{C} \oplus \mathbb{C} \cong \mathbb{C}l_1$.

The even-subalgebra recursion is what makes the classification inductive: it lowers the rank by one and replaces the pair $(p,q)$ by $(q,p-1)$. Iterating it, and using the volume element to decide the split or non-split case at odd rank, produces the tables of Sections 7 and 8.

---

## 10. The dimension and type of the irreducible modules

Over $\mathbb{C}$, the simple modules of $\mathbb{C}l_n$ have complex dimension
$$
\dim_{\mathbb{C}} \Delta = 2^{\lfloor n/2 \rfloor}.
$$
For $n$ even the algebra is simple and $\Delta$ is the unique simple module; for $n$ odd there are two non-isomorphic simple modules, each of that dimension.

Over $\mathbb{R}$, the irreducible modules of $\operatorname{Cl}_{n,0}$ have the following dimensions and types. The **type** is the division algebra $\mathbb{D}$ that commutes with the action, so that the module is a free $\mathbb{D}$-module; by Schur's lemma $\mathbb{D}$ is one of $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$.

| $n$ | $\operatorname{Cl}_{n,0}(\mathbb{R})$ | $\dim_\mathbb{R} S$ | type |
|---|---|---|---|
| 0 | $\mathbb{R}$ | 1 | $\mathbb{R}$ |
| 1 | $\mathbb{R} \oplus \mathbb{R}$ | 1 | $\mathbb{R}$ |
| 2 | $M_2(\mathbb{R})$ | 2 | $\mathbb{R}$ |
| 3 | $M_2(\mathbb{C})$ | 4 | $\mathbb{C}$ |
| 4 | $M_2(\mathbb{H})$ | 8 | $\mathbb{H}$ |
| 5 | $M_2(\mathbb{H}) \oplus M_2(\mathbb{H})$ | 8 | $\mathbb{H}$ |
| 6 | $M_4(\mathbb{H})$ | 16 | $\mathbb{H}$ |
| 7 | $M_8(\mathbb{C})$ | 16 | $\mathbb{C}$ |
| 8 | $M_{16}(\mathbb{R})$ | 16 | $\mathbb{R}$ |

The dimension column lists the **Radon--Hurwitz numbers**. They satisfy
$$
\dim_\mathbb{R} S_{n+8} = 16 \cdot \dim_\mathbb{R} S_n,
$$
which is exactly the effect of tensoring by the $16$-dimensional irreducible $\operatorname{Cl}_8$-module, and the type column has period $8$: the sequence is $\mathbb{R}, \mathbb{R}, \mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{H}, \mathbb{H}, \mathbb{C}$. For an odd-rank algebra that is a sum of two matrix algebras, the irreducible module is a simple module of one factor and the type is read off in the same way.

The derivation is short. When $\operatorname{Cl}_{n,0} \cong M_k(\mathbb{D})$ for a division algebra $\mathbb{D}$, the irreducible module is $\mathbb{D}^k$ and the type is $\mathbb{D}$; when $\operatorname{Cl}_{n,0}$ is a sum of two copies of such a matrix algebra, the same description applies to either summand. The table of Section 7 supplies $k$ and $\mathbb{D}$ at each rank.

---

# Part III: Morita Equivalence and the Brauer--Wall Group

## 11. Morita equivalence

Two algebras $A$ and $B$ are **Morita equivalent** if their categories of modules are equivalent. The basic example is that $A$ and $M_k(A)$ are Morita equivalent, for every $k \geq 1$: the category of $M_k(A)$-modules is the category of $A$-modules, with no essential change. In the graded setting the corresponding statement is that a matrix superalgebra $M_{r|s}(F)$ is graded Morita equivalent to $F$, and the graded tensor product is compatible with the equivalence.

The two relations
$$
\operatorname{Cl}_{p+1,q+1}(\mathbb{R}) \cong \operatorname{Cl}_{p,q}(\mathbb{R}) \otimes_\mathbb{R} M_2(\mathbb{R}), \qquad \operatorname{Cl}_{p+8,q}(\mathbb{R}) \cong \operatorname{Cl}_{p,q}(\mathbb{R}) \otimes_\mathbb{R} M_{16}(\mathbb{R})
$$
show that adjacent Clifford algebras differ by a matrix factor. Passing to graded Morita classes, the matrix factor disappears, and the class of $\operatorname{Cl}_{p,q}$ depends only on $p - q \bmod 8$. Equivalently,
$$
\operatorname{Cl}_{p,q} \text{ and } \operatorname{Cl}_{p',q'} \text{ are graded Morita equivalent} \iff p - q \equiv p' - q' \pmod 8.
$$
This is the precise sense in which the period-$8$ classification is a classification of module categories: the eight residues of $p-q$ are the eight graded Morita classes, while the finer isomorphism type also remembers $n = p+q \bmod 8$.

## 12. The Brauer--Wall group

The set of graded Morita classes of finite-dimensional $\mathbb{Z}/2$-graded central simple algebras over a field $F$, with the graded tensor product as operation, is an abelian group $BW(F)$, the **Brauer--Wall group**. Its elements are the graded Brauer classes, and the class of the Clifford algebra of a form is the **Clifford invariant** of that form.

For the fields of this series the group is
$$
BW(\mathbb{R}) \cong \mathbb{Z}/8, \qquad BW(\mathbb{C}) \cong \mathbb{Z}/2.
$$
Over $\mathbb{R}$, the classes of $\operatorname{Cl}_{0,n}$ for $n = 0, \ldots, 7$ are the eight distinct elements, and $[\operatorname{Cl}_{0,1}]$ is a generator; the fact that $\operatorname{Cl}_{0,8} \cong M_{16}(\mathbb{R})$ is graded Morita equivalent to $\mathbb{R}$ is the relation $8 [\operatorname{Cl}_{0,1}] = 0$. Over $\mathbb{C}$ the invariant is the single bit $n \bmod 2$.

The group $BW(F)$ contains the ordinary Brauer group $Br(F)$ as the subgroup of classes represented by algebras concentrated in even degree. For $F = \mathbb{R}$ this subgroup is $Br(\mathbb{R}) = \mathbb{Z}/2$, and within $BW(\mathbb{R}) = \mathbb{Z}/8$ it is the $2$-torsion subgroup.

Finally, the assignment $q \mapsto [\operatorname{Cl}(q)]$ is additive for orthogonal sums, because $\operatorname{Cl}(q \perp q') \cong \operatorname{Cl}(q) \hat{\otimes} \operatorname{Cl}(q')$, and it vanishes on the hyperbolic plane, whose Clifford algebra is $M_2(F)$, graded Morita equivalent to $F$. It therefore descends to a homomorphism
$$
W(F) \longrightarrow BW(F)
$$
from the Witt group of $F$, the **Clifford invariant**.

## 13. The complex case: period two and one-periodicity

Over $\mathbb{C}$ the graded invariant has period $2$: it is the residue $n \bmod 2$, and $BW(\mathbb{C}) = \mathbb{Z}/2$. There is also a one-step recursion,
$$
\mathbb{C}l_{n+1} \cong \mathbb{C}l_n \hat{\otimes} \mathbb{C}l_1,
$$
with $\mathbb{C}l_1 \cong \mathbb{C} \oplus \mathbb{C}$. Now $\mathbb{C} \oplus \mathbb{C}$ is Morita equivalent to $\mathbb{C}$, since it is a product of two copies of the base field. It follows that, forgetting the grading, $\mathbb{C}l_{n+1}$ is Morita equivalent to $\mathbb{C}l_n$ for every $n$: the ungraded Morita class is constant, that is, **$1$-periodic**. The complex case therefore exhibits both faces at once. Ungraded, its Morita invariant has period one and is trivial, because $Br(\mathbb{C}) = 0$ and every $\mathbb{C}l_n$ is Morita equivalent to $\mathbb{C}$; graded, the same invariant has period two and is the non-trivial element of $BW(\mathbb{C}) = \mathbb{Z}/2$ for odd $n$. This is the precise sense in which the complex case is a one-periodicity, refining the shift-by-two isomorphism of Section 2.

---

# Part IV: Atiyah--Bott--Shapiro and the Eightfold Way

## 14. The Atiyah--Bott--Shapiro periodicity

Let $\mathcal{M}(\operatorname{Cl}_n)$ denote the category of $\mathbb{Z}/2$-graded modules over $\operatorname{Cl}_n$, and let $M_n$ denote the corresponding Grothendieck group. Since
$$
\operatorname{Cl}_{n+8} \cong \operatorname{Cl}_n \hat{\otimes} \operatorname{Cl}_8, \qquad \operatorname{Cl}_8 \cong M_{16}(\mathbb{R}),
$$
tensoring by the irreducible $\operatorname{Cl}_8$-module gives an equivalence of graded module categories
$$
\mathcal{M}(\operatorname{Cl}_{n+8}) \simeq \mathcal{M}(\operatorname{Cl}_n),
$$
and hence an isomorphism of Grothendieck groups $M_{n+8} \cong M_n$. This is the **Atiyah--Bott--Shapiro periodicity theorem** for Clifford modules. The complex analogue is
$$
\mathcal{M}(\mathbb{C}l_{n+2}) \simeq \mathcal{M}(\mathbb{C}l_n), \qquad M^{\mathbb{C}}_{n+2} \cong M^{\mathbb{C}}_n.
$$

The theorem is the algebraic form of Bott periodicity. Atiyah, Bott and Shapiro introduced the groups $M_n$ precisely to exhibit the eightfold periodicity of the real theory, and showed that the coefficient groups of real topological $K$-theory are obtained from them, so that $KO^{-n-8}(\mathrm{pt}) \cong KO^{-n}(\mathrm{pt})$. The complex statement has period two and underlies the two-periodicity of complex topological $K$-theory. The module-level statement recorded at the end of Section 6 is the concrete form of the equivalence.

## 15. The eightfold way of spinor types

The type of the spinor modules is governed by the same periodicity, through the even subalgebra. For a form of signature $(p,q)$ with $n = p+q \geq 1$, the spinor module is a simple module of
$$
\operatorname{Cl}^0_{p,q} \cong \operatorname{Cl}_{q,p-1} \quad (p \geq 1),
$$
and the type is that of the simple module of this Clifford algebra. In the Euclidean case this reduces, by Section 9, to
$$
\operatorname{Cl}^0_{n,0}(\mathbb{R}) \cong \operatorname{Cl}_{0,n-1}(\mathbb{R}),
$$
so the type of the spinor module of $Spin(n)$ is the type of the simple $\operatorname{Cl}_{0,n-1}$-module. The simple-module types of $\operatorname{Cl}_{0,k}$ for $k = 0, \ldots, 7$ are
$$
\mathbb{R}, \; \mathbb{C}, \; \mathbb{H}, \; \mathbb{H}, \; \mathbb{H}, \; \mathbb{C}, \; \mathbb{R}, \; \mathbb{R},
$$
and therefore the type of the spinor module of $Spin(n)$, indexed by $n \bmod 8$, is

| $n \bmod 8$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 |
|---|---|---|---|---|---|---|---|---|
| type | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{H}$ | $\mathbb{H}$ | $\mathbb{H}$ | $\mathbb{C}$ | $\mathbb{R}$ | $\mathbb{R}$ |

This is the **eightfold way** of spinor types: real, complex and quaternionic structures recur with period $8$, and no other period appears. For a general signature the invariant is $s = p - q \bmod 8$, and the standard tables are:

- for $n$ even, the half-spin modules have type $\mathbb{R}$ for $s = 0$, type $\mathbb{C}$ for $s = 2, 6$, and type $\mathbb{H}$ for $s = 4$;
- for $n$ odd, the spinor module has type $\mathbb{R}$ for $s = 1, 7$ and type $\mathbb{H}$ for $s = 3, 5$.

These are the tables of the article *Spinors*, where the consequences for Dirac, Weyl, Majorana and symplectic Majorana spinors are developed.

## 16. Consequences for spinors

The periodicity controls which real structures a spinor module can carry. A real structure, hence a Majorana spinor, exists exactly when the corresponding module is of real type; a quaternionic structure gives a symplectic Majorana condition; and a module of complex type admits neither, although the full spinor module is then self-conjugate. Whether the type is real, complex or quaternionic therefore depends only on $n \bmod 8$ in Euclidean signature, and on $p - q \bmod 8$ in general. The dimension of the spinor module, $2^{\lfloor n/2 \rfloor}$ over $\mathbb{C}$ and the Radon--Hurwitz numbers over $\mathbb{R}$, is likewise periodic with period $8$, while over $\mathbb{C}$ the period is $2$. The eight rows of the table in Section 15 are the eight rows of the real periodicity, read through the even subalgebra.

---

# Summary

Let me summarize the main points.

**The periodicity.** The real Clifford algebras satisfy
$$
\operatorname{Cl}_{n+8}(\mathbb{R}) \cong \operatorname{Cl}_n(\mathbb{R}) \otimes_\mathbb{R} M_{16}(\mathbb{R}),
$$
with the more general forms $\operatorname{Cl}_{p+8,q} \cong \operatorname{Cl}_{p,q} \otimes M_{16}(\mathbb{R})$ and $\operatorname{Cl}_{p,q+8} \cong \operatorname{Cl}_{p,q} \otimes M_{16}(\mathbb{R})$, and the complex ones satisfy
$$
\mathbb{C}l_{n+2} \cong \mathbb{C}l_n \otimes_\mathbb{C} M_2(\mathbb{C}).
$$
The shifts are $8$ and $2$, and the matrix sizes are $16$ and $2$.

**The source.** Both statements follow from the tensor product decomposition $\operatorname{Cl}(M_1 \oplus M_2) \cong \operatorname{Cl}(M_1) \hat{\otimes} \operatorname{Cl}(M_2)$ together with the single computations $\operatorname{Cl}_8 \cong M_{16}(\mathbb{R})$ and $\mathbb{C}l_2 \cong M_2(\mathbb{C})$.

**The volume element.** For an orthogonal basis, $\omega = e_1 \cdots e_n$ satisfies $\omega^2 = (-1)^{n(n-1)/2} Q(e_1) \cdots Q(e_n) \cdot 1$. It is central for odd $n$, and for even $n$ it is the chirality operator whose eigenspaces are the half-spinors.

**The classification.** Up to isomorphism, $\operatorname{Cl}_{p,q}(\mathbb{R})$ depends only on $p+q$ and $p-q$ modulo $8$, while $\mathbb{C}l_n$ depends only on $n \bmod 2$; the even subalgebra recursion $\operatorname{Cl}^0_{p,q} \cong \operatorname{Cl}_{q,p-1}$ makes the classification inductive.

**The modules.** The complex spinor module has dimension $2^{\lfloor n/2 \rfloor}$; over $\mathbb{R}$ the irreducible dimensions are the Radon--Hurwitz numbers, with $\dim_\mathbb{R} S_{n+8} = 16 \dim_\mathbb{R} S_n$, and the type is $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$ according to $n \bmod 8$.

**The Brauer--Wall group.** Passing to graded Morita classes, $\operatorname{Cl}_{p,q}$ depends only on $p-q \bmod 8$; the classes form $BW(\mathbb{R}) = \mathbb{Z}/8$ and $BW(\mathbb{C}) = \mathbb{Z}/2$, and $q \mapsto [\operatorname{Cl}(q)]$ is the Clifford invariant $W(F) \to BW(F)$. Ungraded, the complex case is $1$-periodic, since $\mathbb{C}l_1$ is Morita equivalent to $\mathbb{C}$ and $Br(\mathbb{C}) = 0$.

**Atiyah--Bott--Shapiro.** The periodicity is the equivalence $\mathcal{M}(\operatorname{Cl}_{n+8}) \simeq \mathcal{M}(\operatorname{Cl}_n)$, with complex analogue $\mathcal{M}(\mathbb{C}l_{n+2}) \simeq \mathcal{M}(\mathbb{C}l_n)$. It yields the eightfold periodic table of real, complex and quaternionic spinor types, and so governs which Majorana, Weyl and symplectic Majorana spinors exist in each dimension.

---

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the periodicity, the module theory and the analytic applications.
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the definitive modern classification.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the tables of low-dimensional Clifford algebras and spinors.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Clifford invariant and the Brauer--Wall group.
- Dale Husemoller, *Fibre Bundles* (Springer, 3rd ed. 1994), for Clifford modules, the Atiyah--Bott--Shapiro periodicity and Bott periodicity.
- Paolo Budinich and Andrzej Trautman, *The Spinorial Chessboard* (Springer, 1988), for the eightfold way of spinor types.
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978), for the topological periodicity that the algebraic periodicity underlies.
