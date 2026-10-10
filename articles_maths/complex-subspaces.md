
# __Complex Subspaces__

## Introduction

The complex algebra $\mathbb{C}$, regarded as a two-dimensional algebra over $\mathbb{R}$, carries exactly one nontrivial involution, complex conjugation, and beside it the identity. Each of the two involutions determines a fixed subspace and an anti-fixed subspace, and the algebra splits as their direct sum. The whole of this article is the analysis of those subspaces: their bases, their dimensions, their closure properties, the quadratic form they inherit, and the sense in which they are the one-dimensional analogue of the remarkable-subspace lattice of the biquaternion algebra $\mathbb{B}$.

The algebra and its conventions are those of the companion article *Complex Algebra*: the basis is $1$, $i$ with $i^2 = -1$, a general element is $A = a + i a'$, and the norm is $N(A) = A\bar{A} = a^2 + a'^2$. The algebra is a field, so it has no proper ideals and no zero divisors; the biquaternion algebra $\mathbb{B}$ is the four-dimensional complex algebra whose remarkable subspaces are the model this article is measured against, and the difference between the two lattices is the point. The two involutions are treated in the article *Complex Automorphisms and Derivations*, where they are the automorphism group of the algebra; here they are used only to cut the algebra into subspaces.

## The Involutions and the Two Decompositions

**Definition.** An **involution** of $\mathbb{C}$ is an $\mathbb{R}$-linear map $\sigma : \mathbb{C} \to \mathbb{C}$ with $\sigma^2 = \operatorname{id}$. Its **fixed subspace** and **anti-fixed subspace** are

$$
\mathbb{C}^{\sigma} = \{ A \in \mathbb{C} : \sigma(A) = A \}, \qquad \mathbb{C}^{-\sigma} = \{ A \in \mathbb{C} : \sigma(A) = -A \}.
$$

The two natural involutions are the identity and complex conjugation:

$$
\operatorname{id}(A) = A, \qquad \bar{\cdot}(A) = \bar{A} = a - i a' .
$$

**Proposition (eigenspace decomposition).** For any involution $\sigma$ of $\mathbb{C}$,

$$
\mathbb{C} = \mathbb{C}^{\sigma} \oplus \mathbb{C}^{-\sigma}, \qquad
A = \tfrac{1}{2}\bigl(A + \sigma(A)\bigr) + \tfrac{1}{2}\bigl(A - \sigma(A)\bigr).
$$

**Proof.** The element $\tfrac{1}{2}(A+\sigma A)$ is fixed because $\sigma^2 = \operatorname{id}$, and $\tfrac{1}{2}(A-\sigma A)$ is anti-fixed, so the sum is $A$ and the two subspaces span. If $A$ lies in both then $A = -A$, hence $2A = 0$ and $A = 0$ because $\mathbb{R}$ has characteristic not $2$, so the sum is direct. Equivalently, the decomposition is the spectral decomposition of $\sigma$ into its eigenspaces for the eigenvalues $+1$ and $-1$.

The two involutions therefore give two decompositions of the algebra:

| involution | fixed subspace | anti-fixed subspace | decomposition |
|---|---|---|---|
| $\operatorname{id}$ | $\mathbb{C}$ | $\{0\}$ | $\mathbb{C} = \mathbb{C} \oplus \{0\}$ |
| $\bar{\cdot}$ | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ |

The identity is degenerate: its fixed subspace is the whole algebra and its anti-fixed subspace is the origin. The decomposition of content is the second row, the decomposition of an element into a real part and an imaginary part. It is the only decomposition of the algebra produced by its involutions, and the reason the lattice below has two members rather than six.

## The Two Subspaces at a Glance

**Definition.** The **real subspace** and the **imaginary subspace** of $\mathbb{C}$ are

$$
\mathbb{R}_{\mathbb{C}} = \{ A \in \mathbb{C} : \bar{A} = A \}, \qquad i\mathbb{R}_{\mathbb{C}} = \{ A \in \mathbb{C} : \bar{A} = -A \}.
$$

**Proposition (bases and dimensions).** In the basis $1$, $i$,

$$
\mathbb{R}_{\mathbb{C}} = \{ a : a \in \mathbb{R} \} = \mathbb{R} 1, \qquad
i\mathbb{R}_{\mathbb{C}} = \{ i a' : a' \in \mathbb{R} \} = \mathbb{R} i,
$$

so each has real dimension $1$ and $\dim_{\mathbb{R}} \mathbb{C} = 1 + 1 = 2$.

**Proof.** If $A = a + i a'$ is fixed by conjugation then $a - i a' = a + i a'$, so $a' = 0$; if it is anti-fixed then $a - i a' = -(a+i a')$, so $a = 0$. The two conditions define the two coordinate axes, of dimension one each.

The two subspaces could hardly be more different in their multiplicative behaviour. The real subspace is closed under multiplication and is a field; the imaginary subspace is not closed at all.

**Proposition (the real subspace is a subfield).** $\mathbb{R}_{\mathbb{C}}$ is a subalgebra of $\mathbb{C}$, and the map $a \mapsto a$ is an isomorphism of fields $\mathbb{R}_{\mathbb{C}} \cong \mathbb{R}$. It is an ordered field under the inherited order.

**Proof.** The product of two fixed elements is fixed, since $\overline{AB} = \bar{A}\bar{B}$, and the multiplicative identity $1$ is fixed, so $\mathbb{R}_{\mathbb{C}}$ is a subalgebra. The map is a ring isomorphism onto $\mathbb{R}$ by the multiplication rule $(a)(b) = ab$, and the restriction of the ordering of $\mathbb{R}$ makes it ordered.

**Proposition (the imaginary subspace is not closed).** $i\mathbb{R}_{\mathbb{C}}$ is not closed under multiplication. For $A, B \in i\mathbb{R}_{\mathbb{C}}$ neither $AB$ nor $A^2$ need lie in $i\mathbb{R}_{\mathbb{C}}$; in fact

$$
(i a')(i b') = -a' b' \in \mathbb{R}_{\mathbb{C}}, \qquad (i a')^2 = -a'^2 \in \mathbb{R}_{\mathbb{C}},
$$

so the product of two anti-fixed elements is fixed.

**Proof.** The rule $i^2 = -1$ gives both displays directly; the right-hand sides are real and nonzero for $a'$ and $b'$ nonzero, so the product leaves the imaginary subspace.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra | norm |
|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $\bar{A} = A$ | $1$ | $1$ | yes, $\cong \mathbb{R}$, a field | $a^2$, definite positive |
| $i\mathbb{R}_{\mathbb{C}}$ | $\bar{A} = -A$ | $i$ | $1$ | no | $a'^2$, definite positive |

The last column records that the norm is positive on each subspace; this is the degeneracy of the definite two-dimensional case and is developed in the last section but one.

## The Two Coordinate Blocks

Writing $A = a + i a'$, the two real coordinates $(a, a')$ group into the two lines

$$
\mathbb{R}_{\mathbb{C}} = \langle 1 \rangle, \qquad i\mathbb{R}_{\mathbb{C}} = \langle i \rangle,
$$

and these are the **coordinate blocks** of $\mathbb{C}$. There are two of them, each of dimension one, and each of the two subspaces is a single block; no subspace of the lattice is a sum of two blocks. This is the structural difference from the biquaternion algebra, whose eight real coordinates form four blocks $\langle e_0 \rangle$, $\langle e_1, e_2, e_3 \rangle$, $\langle i e_1, i e_2, i e_3 \rangle$, $\langle i e_0 \rangle$ from which the remarkable subspaces are assembled.

The block description makes the intersection and sum arithmetic below immediate: two subspaces meet nontrivially only if they share a block, and here the only shared blocks are the blocks they are.

## The Intersections

The pairwise intersections of the two subspaces are read off from the blocks:

| | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $1$ | $0$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $0$ | $1$ |

**Proposition.** $\mathbb{R}_{\mathbb{C}} \cap i\mathbb{R}_{\mathbb{C}} = \{0\}$.

**Proof.** An element of the intersection is both fixed and anti-fixed by conjugation, so $A = -A$ and $A = 0$ in characteristic not $2$; alternatively the two subspaces are the coordinate lines $\langle 1 \rangle$ and $\langle i \rangle$, which are independent.

The diagonal of the table carries the dimensions $1$ and $1$; the off-diagonal entry is $0$ because the two subspaces are the two members of a direct-sum decomposition. In the biquaternion lattice the analogous entry is also $0$ for the pairs of each decomposition, but there the off-diagonal entries can be $1$ or $3$ because subspaces assembled from several blocks can share a block.

## The Sums

| | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $1$ | $2$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $2$ | $1$ |

**Proposition.** $\mathbb{R}_{\mathbb{C}} + i\mathbb{R}_{\mathbb{C}} = \mathbb{C}$.

**Proof.** Every $A = a + i a'$ is the sum of $a \in \mathbb{R}_{\mathbb{C}}$ and $i a' \in i\mathbb{R}_{\mathbb{C}}$, and the sum is direct by the previous proposition.

The single off-diagonal entry is $2 = \dim_{\mathbb{R}} \mathbb{C}$: the two subspaces together span the algebra, exactly as the members of each decomposition do in $\mathbb{B}$. There is no second distinct pair and hence no larger body of sum arithmetic.

## The Involutions as Sign Patterns

Each involution preserves each subspace and acts on it by a scalar, $+1$ or $-1$. The multiplicities of the sign $-1$ are:

| involution | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
|---|---|---|
| $\operatorname{id}$ | $0$ of $1$ | $0$ of $1$ |
| $\bar{\cdot}$ | $0$ of $1$ | $1$ of $1$ |

The identity negates nothing; conjugation negates the imaginary line and fixes the real one. The vanishing entries are the definitions of the fixed subspaces, and the full entry is the definition of the anti-fixed one. Because there are only two involutions and two one-dimensional subspaces, the sign pattern carries no mixed restrictions, in contrast with the four-involution table of $\mathbb{B}$ where the mixed entries measure the failure of the involutions to be pointwise equal.

## How the Operations Act on the Splits

### Multiplication by the Imaginary Unit

Multiplication by $i$ exchanges the two subspaces:

$$
i\,\mathbb{R}_{\mathbb{C}} = i\mathbb{R}_{\mathbb{C}}, \qquad i\, i\mathbb{R}_{\mathbb{C}} = \mathbb{R}_{\mathbb{C}}.
$$

The first identity says that the real axis is carried to the imaginary axis, the second that the imaginary axis is carried back; the operator $A \mapsto i A$ is therefore a real-linear map of order four with square $-1$, the complex structure of the algebra. It is the placement, in the two-dimensional case, of the block exchange recorded for $\mathbb{B}$.

### The Product and the Brackets

**Proposition (product table).** For elements taken from the two subspaces, the product falls as follows.

| product | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ |

**Proof.** The products $1\cdot 1 = 1$, $1\cdot i = i$, $i\cdot 1 = i$ and $i^2 = -1$ are the multiplication table of the basis.

Since $\mathbb{C}$ is commutative, every commutator vanishes:

$$
[A, B] = AB - BA = 0 \qquad (A, B \in \mathbb{C}),
$$

so the commutator bracket produces no subspace, and the symmetrized product $AB + BA = 2AB$ produces no subspace beyond the product itself. The Lie-algebra slot of the biquaternion table, occupied there by the vector subspace $\mathrm{Vect}(\mathbb{B})$ under the commutator, is empty here. This emptiness is a mathematical statement: it is the commutativity of the field, and it is why the derivation space of $\mathbb{C}$ vanishes while that of $\mathbb{B}$ does not.

## Worked Verifications

**A generic element.** For $A = 3 + 4i$ the eigencomponents of conjugation are

$$
A_+ = \tfrac{1}{2}(A + \bar{A}) = 3 \in \mathbb{R}_{\mathbb{C}}, \qquad
A_- = \tfrac{1}{2}(A - \bar{A}) = 4i \in i\mathbb{R}_{\mathbb{C}},
$$

with $A_+ + A_- = 3 + 4i = A$, and the norm on the pieces is $N(A_+) = 9$ and $N(A_-) = 16$, whose sum $25 = N(A)$ is the norm of $A$. The two blocks are the real coordinate $3$ and the imaginary coordinate $4$.

**A product that leaves a subspace.** For $A_- = 4i$ and $B_- = 5i$, both in $i\mathbb{R}_{\mathbb{C}}$,

$$
A_- B_- = (4i)(5i) = 20\, i^2 = -20 \in \mathbb{R}_{\mathbb{C}},
$$

so the product of two anti-fixed elements is fixed and nonzero. The commutator is $A_- B_- - B_- A_- = 0$, consistent with the vanishing bracket of the previous section.

**An intersection.** If $A = a + i a'$ lies in both $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$ then $a' = 0$ and $a = 0$, so $A = 0$; the intersection is the origin, as the table records.

## Summary

The complex algebra carries exactly one nontrivial involution, complex conjugation, and beside it the identity. Conjugation splits the algebra as $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ into its fixed subspace, the real axis $\mathbb{R}_{\mathbb{C}} = \mathbb{R} 1$ of real dimension one, and its anti-fixed subspace, the imaginary axis $i\mathbb{R}_{\mathbb{C}} = \mathbb{R} i$, also of real dimension one. The identity is degenerate, with fixed subspace the whole algebra and anti-fixed subspace the origin.

The real subspace is closed under multiplication and is a field isomorphic to $\mathbb{R}$; the imaginary subspace is not closed, since the product of two of its elements is real, $(i a')(i b') = -a' b'$. The two subspaces meet only in the origin and together span the algebra. They are the two coordinate blocks of the real basis, and multiplication by $i$ exchanges them.

The lattice is the two-member shadow of the remarkable-subspace lattice of the biquaternion algebra: the two blocks $\langle 1 \rangle$ and $\langle i \rangle$ of the two coordinates replace the four blocks of the eight real coordinates of $\mathbb{B}$, and the four involutions of $\mathbb{B}$ collapse to the single nontrivial involution of $\mathbb{C}$. The commutator bracket vanishes identically because the algebra is commutative, so the vector subspace of $\mathbb{B}$ and its Lie-algebra structure have no analogue here; that absent slot is the commutativity of the field.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $A = a + i a'$ | a complex number |
| $\operatorname{id}$, $\bar{\cdot}$ | the identity and the nontrivial involution, complex conjugation |
| $\mathbb{C}^{\sigma}$, $\mathbb{C}^{-\sigma}$ | fixed and anti-fixed subspaces of an involution $\sigma$ |
| $\mathbb{R}_{\mathbb{C}}$ | real subspace $\{A : \bar{A} = A\} = \mathbb{R} 1$, real dimension $1$ |
| $i\mathbb{R}_{\mathbb{C}}$ | imaginary subspace $\{A : \bar{A} = -A\} = \mathbb{R} i$, real dimension $1$ |
| $N(A) = A\bar{A} = a^2 + a'^2$ | the norm |
| $i\,\cdot$ (multiplication by $i$) | exchanges the two subspaces: $\mathbb{R}_{\mathbb{C}} \to i\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}} \to \mathbb{R}_{\mathbb{C}}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the real and imaginary axes of the plane.
- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the geometric reading of the two coordinates.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for involutions, eigenspace decompositions and subfields.
- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for the algebraic closure and the real and imaginary parts of a quadratic extension.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the real and imaginary subspaces of a two-dimensional definite algebra and their higher-dimensional analogues.
