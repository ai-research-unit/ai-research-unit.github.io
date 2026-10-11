# __Decompositions and Comparison of the Remarkable Subspaces of the Complex Numbers__

## Introduction

The complex algebra carries one nontrivial involution, complex conjugation, and beside it the identity, and each of the two cuts the algebra into a fixed subspace and an anti-fixed subspace. This article writes the two decompositions those involutions produce, with their projections, records how the product and the two forms behave along the split, and compares the resulting two-member lattice with the six remarkable subspaces of the biquaternion algebra $\mathbb{B}$, ending with the collapse of the six to two that commutativity forces.

The subspaces themselves, their bases and their dimensions are the subject of *Complex Subspaces*, which this article cites and does not repeat; the two forms are the subject of *The Two Forms and the Two Algebraic Norms of the Complex Space*, and the products are *The Two Products of the Complex Space*, both below this article in this category. What is new here is the frame: the two decompositions read as the degenerate and the content-bearing case, the behaviour of the products and the forms along that split, and the comparison with the biquaternion lattice.

The reading of the marks is the corpus convention: the **bar** is complex conjugation, the one nontrivial involution of $\mathbb{C}$; the **natural sign** is the identity, there being no quaternion factor on a commutative base; and the **Hermitian star** coincides with the bar. The two "natural conjugations" of *Complex Algebra*, below this article in this category, are the identity and the bar.

## The Two Involutions and Their Decompositions

An involution of $\mathbb{C}$ is an $\mathbb{R}$-linear map $\sigma$ with $\sigma^2 = \operatorname{id}$, and its **fixed** and **anti-fixed** subspaces are

$$
\mathbb{C}^{\sigma} = \{ A : \sigma(A) = A \}, \qquad \mathbb{C}^{-\sigma} = \{ A : \sigma(A) = -A \} .
$$

The two involutions are the identity and the bar. Each gives a decomposition into its eigenlines for the eigenvalues $+1$ and $-1$:

$$
\mathbb{C} = \mathbb{C}^{\sigma} \oplus \mathbb{C}^{-\sigma}, \qquad A = \tfrac{1}{2}\bigl(A + \sigma(A)\bigr) + \tfrac{1}{2}\bigl(A - \sigma(A)\bigr) .
$$

In the basis $1, i$ the two read as follows.

| involution | fixed subspace | anti-fixed subspace | decomposition | dimension |
|---|---|---|---|---|
| $\operatorname{id}$ | $\mathbb{C}$ | $\{0\}$ | $\mathbb{C} = \mathbb{C} \oplus \{0\}$ | $2 = 2 + 0$ |
| $\bar{\cdot}$ | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ | $2 = 1 + 1$ |

The decomposition of the identity is degenerate: its fixed subspace is the whole algebra and its anti-fixed subspace the origin, and its two projections are the identity and the zero map. The decomposition of the bar is the one that carries content; its projections are

$$
A \longmapsto \tfrac{1}{2}\bigl(A + \bar A\bigr) = a \in \mathbb{R}_{\mathbb{C}}, \qquad
A \longmapsto \tfrac{1}{2}\bigl(A - \bar A\bigr) = i a' \in i\mathbb{R}_{\mathbb{C}} .
$$

These are the two halves of the developed form $A = a + i a'$, and the sum of the two projections is $A$. The article *Decompositions Along the Remarkable Subspaces* of the biquaternion chapter has the same shape with the three commuting involutions of $\mathbb{B}$ and their three decompositions; here two involutions suffice, and one of the two decompositions is degenerate, which is the first and largest difference from the biquaternion case.

## The Product Along the Split

The two products of the complex space are the plain product $AC$, the multiplication of the field, and the plain sesquilinear product $A\bar C$, both defined in *The Two Products of the Complex Space*, below this article in this category. Their behaviour on elements drawn from the two subspaces is read from the multiplication table of the basis.

| product | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{C}}$ |

**Proposition.** Both products send a pair of subspaces to the same subspace as the plain product does. The sesquilinear product differs from the plain one only by the sign carried by the second slot, and

$$
A\bar C = AC \text{ if } C \in \mathbb{R}_{\mathbb{C}}, \qquad A\bar C = -AC \text{ if } C \in i\mathbb{R}_{\mathbb{C}} .
$$

**Proof.** The bar fixes $\mathbb{R}_{\mathbb{C}}$ pointwise and negates $i\mathbb{R}_{\mathbb{C}}$, so $\bar C = C$ in the first case and $\bar C = -C$ in the second; the subspace table is unchanged because a sign does not move an element out of a subspace and because a line through the origin is closed under sign.

The product table is the multiplication table of $1, i$, $1\cdot 1 = 1$, $1\cdot i = i$, $i\cdot i = -1$; it is the table owned by *Complex Subspaces*, and the sesquilinear reading above is the only addition this article makes to it. Two features of the complex case are immediate. The product of a real and an imaginary element stays imaginary, and the product of two imaginary elements is real, so the imaginary subspace is not closed under either product while its square lands in the real one. And because $\mathbb{C}$ is commutative, every commutator vanishes, $[A, C] = AC - CA = 0$, so the antisymmetric product produces no subspace; the Lie-algebra slot that carries the vector subspace of $\mathbb{B}$ is empty here.

## The Two Forms Along the Split

The forms carried by the two products are the plain bilinear form $B$ and the Hermitian form $H$, defined on a pair by

$$
B(A, C) = AC, \qquad H(A, C) = A\bar C ,
$$

with the names and the two algebraic norms owned by *The Two Forms and the Two Algebraic Norms of the Complex Space*, below this article in this category. Read along the split, the two forms agree on the real subspace and differ by a sign on the imaginary one:

$$
B = H = AC \text{ on } \mathbb{R}_{\mathbb{C}} \times \mathbb{R}_{\mathbb{C}}, \qquad B = -H \text{ on } i\mathbb{R}_{\mathbb{C}} \times i\mathbb{R}_{\mathbb{C}} .
$$

Their diagonals are the two algebraic norms, $B(A) = A^2$ and $H(A) = \lvert A \rvert^2 = A\bar A$. On the real subspace $A^2$ and $\lvert A \rvert^2$ coincide and are positive; on the imaginary subspace they are opposite, $A^2 = -a'^2$ against $\lvert A \rvert^2 = a'^2$. The full restriction table is the subject of *Remarkable Subspaces of the Complex Numbers and the Two Forms*, below this article in this category; here only the signs along the split are recorded, since they are what the decomposition produces.

## The Two-Member Lattice Against the Biquaternion Six

The biquaternion algebra has six remarkable subspaces. The definitions and the dimensions are those of *Introduction to the Remarkable Subspaces*; the comparison is:

| lattice | subspaces | real dimensions | closed under the product | units with inverses inside |
|---|---|---|---|---|
| $\mathbb{C}$ | $2$ | $1, 1$ | $\mathbb{R}_{\mathbb{C}}$, a field | the nonzero elements of $\mathbb{R}_{\mathbb{C}}$ |
| $\mathbb{B}$ | $6$ | $2, 6, 4, 4, 4, 4$ | $\mathbb{C}_{\mathbb{B}}$, a field; $\mathbb{H}_{\mathbb{B}}$, a division algebra | the nonzero elements of $\mathbb{C}_{\mathbb{B}}$ and of $\mathbb{H}_{\mathbb{B}}$ |

The two complex subspaces are the real line $\mathbb{R}_{\mathbb{C}}$ and the imaginary line $i\mathbb{R}_{\mathbb{C}}$, each of real dimension one. Only the real one is closed under the product, and it is closed in the strongest sense: it is a subalgebra and a field isomorphic to $\mathbb{R}$, its identity $1$ lies in it, and its nonzero elements are units whose inverses lie in it. The imaginary line is not closed, the product of two of its elements being real, and it contains no identity, so it is not a subalgebra; it is nevertheless stable under inversion, the inverse of a nonzero $ia'$ being $-i/a' = i(-1/a')$, again in $i\mathbb{R}_{\mathbb{C}}$. The complex lattice therefore holds one subalgebra, the real line, and one subspace that is not a subalgebra and yet is stable under inversion, the imaginary line; the two properties are separated, and the coincidence that the field $\mathbb{R}_{\mathbb{C}}$ is both is the reason the real line is the distinguished one.

The biquaternion lattice is the six subspaces $\mathbb{C}_{\mathbb{B}}$ the centre, $\mathrm{Vect}(\mathbb{B})$ the vector subspace, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_+$ and $\mathbb{M}_-$, with the dimensions in the table. Of the six, exactly two are closed under the product: the centre $\mathbb{C}_{\mathbb{B}}$, a field isomorphic to $\mathbb{C}$, and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, a division algebra, each with its nonzero elements units whose inverses stay in the subspace; the other four are not closed. Closure and units are the properties the complex lattice keeps in reduced form, one closed subspace against two. The property the complex lattice does not have at all is an isotropic element: the complex form is definite, so no nonzero element of $\mathbb{C}$ has vanishing norm and no subspace of it holds one, whereas $\mathbb{B}$ has its null cone, the null set of its complex norm, a complex cone of real dimension six. Three of the six meet that cone, the vector subspace and the two Hermitian subspaces; the centre and the two quaternion subspaces are anisotropic. That definite character is the reason the complex algebra is a field, with no zero divisors, and it is the deepest difference between the two lattices. The product tables of the biquaternion subspaces are *Remarkable Subspaces and the Four General Products*, in the biquaternion chapter.

## The Collapse of the Six Subspaces to Two

The six biquaternion subspaces are assembled from four real coordinate blocks,

$$
A_1 = \mathbb{R}e_0, \quad A_2 = \mathbb{R}(ie_0), \quad B_1 = \operatorname{span}\{e_1, e_2, e_3\}, \quad B_2 = \operatorname{span}\{ie_1, ie_2, ie_3\} ,
$$

each of the six being the sum of two of the four. The complex lattice is assembled from two blocks, $\langle 1 \rangle$ and $\langle i \rangle$. Under the identification of $\mathbb{C}$ with the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{R}e_0 \oplus \mathbb{R}(ie_0)$, the two complex blocks are the two central blocks of the biquaternion algebra:

| biquaternion block | complex block |
|---|---|
| $A_1 = \mathbb{R}e_0$ | $\langle 1 \rangle$ |
| $A_2 = \mathbb{R}(ie_0)$ | $\langle i \rangle$ |
| $B_1 = \operatorname{span}\{e_1, e_2, e_3\}$ | — |
| $B_2 = \operatorname{span}\{ie_1, ie_2, ie_3\}$ | — |

The blocks $B_1$ and $B_2$ are the quaternionic directions, spanned by the non-central units $e_1, e_2, e_3$ and their multiples by $i$; the complex algebra has no non-central directions, since every element commutes with every other, and the two blocks therefore have no image. The six subspaces, written as sums of blocks, reduce as follows.

| biquaternion subspace | blocks | complex image |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | $A_1 \oplus A_2$ | $\mathbb{C}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ | $\{0\}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1 \oplus B_1$ | $\mathbb{R}_{\mathbb{C}}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2 \oplus B_2$ | $i\mathbb{R}_{\mathbb{C}}$ |
| $\mathbb{M}_+$ | $A_1 \oplus B_2$ | $\mathbb{R}_{\mathbb{C}}$ |
| $\mathbb{M}_-$ | $A_2 \oplus B_1$ | $i\mathbb{R}_{\mathbb{C}}$ |

The collapse is the algebraic statement of commutativity. Dropping the two quaternionic blocks is dropping the non-central directions, and a non-central direction is exactly what a commutative algebra does not have; the six subspaces, of dimensions $2, 6, 4, 4, 4, 4$, are reduced to the two lines of dimensions $1$ and $1$, and the three commuting involutions of $\mathbb{B}$ to the two involutions of $\mathbb{C}$, the identity and the bar. The biquaternion patterns are *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, in the biquaternion chapter.

## Summary

The complex algebra carries two involutions, the identity and the bar, and each gives an eigenline decomposition. The decomposition of the identity is degenerate, $\mathbb{C} = \mathbb{C} \oplus \{0\}$, with projections the identity and the zero map; the decomposition of the bar is the content-bearing one, $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$, with projections $A \mapsto \tfrac{1}{2}(A+\bar A)$ onto the real line and $A \mapsto \tfrac{1}{2}(A-\bar A)$ onto the imaginary line.

Along the split, the two products $AC$ and $A\bar C$ send the same pairs of subspaces to the same subspaces as the plain product, and the sesquilinear product differs from the plain one by the sign of the second slot, which the bar fixes on the real line and negates on the imaginary line. The two forms $B$ and $H$ agree on the real subspace and are opposite on the imaginary one, and their diagonals $A^2$ and $\lvert A \rvert^2$ coincide and are positive on the real line and are opposite on the imaginary line. The commutator vanishes identically, so the antisymmetric product produces no subspace.

Compared with the six remarkable subspaces of the biquaternion algebra, the two complex subspaces are the two-member shadow: one subalgebra, the field $\mathbb{R}_{\mathbb{C}}$, and one line that is stable under inversion but is not a subalgebra, against the two subalgebras among the six, and no isotropic element at all, the complex form being definite where the biquaternion norm has its null cone. The biquaternion lattice is assembled from four coordinate blocks and the complex one from two, the two surviving blocks being the central ones $A_1$ and $A_2$; the two quaternionic blocks $B_1$ and $B_2$ have no image because the complex algebra has no non-central directions. The six subspaces reduce to the two lines, and the three commuting involutions of $\mathbb{B}$ reduce to the two of $\mathbb{C}$, the identity and the bar.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\sigma$, $\mathbb{C}^{\sigma}$, $\mathbb{C}^{-\sigma}$ | an involution, its fixed subspace and its anti-fixed subspace |
| $\operatorname{id}, \bar{\cdot}$ | the identity and the bar, the two involutions of $\mathbb{C}$ |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary lines, of real dimension one each |
| $A \mapsto \tfrac{1}{2}(A \pm \bar A)$ | the two projections of the bar decomposition |
| $AC$, $A\bar C$ | the plain bilinear product and the plain sesquilinear product |
| $B, H$ | the plain bilinear form and the Hermitian form, $B = AC$, $H = A\bar C$ |
| $A^2, \lvert A \rvert^2$ | the two algebraic norms, the diagonals of $B$ and of $H$ |
| $A_1, A_2, B_1, B_2$ | the four biquaternion coordinate blocks |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | the six remarkable subspaces of $\mathbb{B}$ |

## Further Reading

- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for involutions, eigenspace decompositions and subfields.
- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for the decomposition of a vector space under an involution and the associated projections.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the real and complex division algebras and the definite forms that single out $\mathbb{C}$.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the coordinate blocks of a real algebra and the subspaces they generate.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the real and imaginary coordinate lines of the plane.
