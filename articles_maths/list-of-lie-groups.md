
# __List of Lie Groups__

## Introduction

This article lists the Lie groups of the corpus, each with its Lie algebra, its real dimension, its rank and the article that introduces it. The list is organised by the two structures a Lie group carries at once. As a manifold it carries a dimension and, when it is connected and compact, a maximal torus whose dimension is its rank; as a group it carries a Lie algebra, obtained as the tangent space at the identity with the bracket of left-invariant vector fields, and the correspondence between the group and the algebra — local by the exponential map and the Campbell–Baker–Hausdorff formula, global for simply connected groups — is the subject of a chain of articles of Parts I to III.

The list begins with the classical matrix groups, which are the examples every later construction names, and continues with the abelian, nilpotent and semidirect examples, with the simple groups and their algebras by type, and with the correspondence itself. Every entry points to the article that introduces the group or the algebra.

The article introduces nothing and proves nothing: it records the dimension and the rank where the introducing article supplies them, and it neither restates a definition nor gives a proof. It records examples and non-examples side by side. Beside the groups that are Lie groups it lists the spheres that are not — only $S^0$, $S^1$ and $S^3$ admit a Lie group structure, so $S^7$ does not — the irrational line of the torus, which is a subgroup but not a Lie subgroup, the quotient by a non-closed subgroup, which is not a manifold, the exponential map, which is not surjective for $SL_2(\mathbb{R})$, and the matrix groups, which fail the correspondence's global form when they are not simply connected, each with the failure named and the article that records it.

## The Classical Matrix Groups

These are the closed subgroups of the general linear groups defined by polynomial or rational conditions, and their dimensions are the dimensions of the defining conditions. All are over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ unless a field is named.

| Group | Real dimension | Its structure | Introduced in |
|---|---|---|---|
| $GL_n(\mathbb{R})$ | $n^2$ | not connected, not compact; the open set $\det \neq 0$ | *Lie Groups* |
| $GL_n(\mathbb{C})$ | $2n^2$ | connected, not compact; the group of units of $M_n(\mathbb{C})$ | *Lie Groups* |
| $SL_n(\mathbb{R})$ | $n^2 - 1$ | connected, not compact; the kernel of the determinant | *Lie Groups* |
| $SL_n(\mathbb{C})$ | $2n^2 - 2$ | connected and simply connected | *Lie Groups* |
| $O(n)$ | $n(n-1)/2$ | compact, two components; identity component $SO(n)$ | *Lie Groups* |
| $SO(n)$ | $n(n-1)/2$ | compact connected; $\pi_1 = \mathbb{Z}/2$ for $n \geq 3$ | *Lie Groups*; *The Orthogonal Lie Algebra* |
| $U(n)$ | $n^2$ | compact connected; $\pi_1 = \mathbb{Z}$ | *Lie Groups* |
| $SU(n)$ | $n^2 - 1$ | compact, connected and simply connected | *Lie Groups* |
| $Sp(n)$ | $n(2n+1)$ | compact, connected and simply connected; the quaternionic unitary group | *Lie Groups* |
| $Sp(2n,\mathbb{R})$ | $n(2n+1)$ | the real symplectic group, $A^TJA = J$ | *Lie Groups* |
| $S^1 = U(1) = SO(2)$ | $1$ | compact connected abelian; $\pi_1 = \mathbb{Z}$ | *Lie Groups* |
| $S^3 = SU(2) = Sp(1)$ | $3$ | compact, connected and simply connected; the unit quaternions | *Lie Groups* |
| $\operatorname{Spin}(n)$, $n \geq 3$ | $n(n-1)/2$ | compact, connected and simply connected; the double cover of $SO(n)$ | *Lie Groups*; *List of Clifford Algebras and Spin Groups* |
| $\mathbb{B}^\times \cong GL_2(\mathbb{C})$ | $8$ | the units of the biquaternion algebra, a real Lie group | *Lie Groups*; *Biquaternion Algebra* |

## The Abelian, Nilpotent and Semidirect Examples

The elementary Lie groups come from vector spaces, from their quotients by lattices and from semidirect products of a linear part with a translation part.

| Group | Real dimension | Its structure | Introduced in |
|---|---|---|---|
| $\mathbb{R}^n$ | $n$ | abelian, simply connected, not compact | *Lie Groups* |
| $\mathbb{C}^n$ | $2n$ | abelian as a real Lie group | *Lie Groups* |
| the torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ | $n$ | compact connected abelian; $\pi_1 = \mathbb{Z}^n$ | *Lie Groups* |
| the Heisenberg group $H_3(\mathbb{R})$ | $3$ | simply connected nilpotent, of class $2$ | *Lie Groups* |
| the Euclidean group $\mathbb{R}^n \rtimes SO(n)$ | $n(n-1)/2 + n$ | the semidirect product of the translations and the rotations | *Lie Groups*; *List of Affine and Euclidean Groups* |
| the affine group $\mathbb{R}^n \rtimes GL_n(\mathbb{R})$ | $n^2 + n$ | the automorphism group of affine $n$-space | *List of Affine and Euclidean Groups* |
| the Lorentz group $O(1,3)$ | $6$ | the isometry group of Minkowski space; $SO^+(1,3)$ has cover $SL_2(\mathbb{C})$ | *Lie Groups*; *Pseudo-Riemannian and Lorentzian Geometry* |
| $S^3/\{\pm1\} \cong SO(3) \cong \mathbb{RP}^3$ | $3$ | compact connected, not simply connected | *Lie Groups* |
| the complex and quaternionic unit spheres | $2n-1$ and $4n-1$ | closed under multiplication only for $n = 1$ in the complex case, and for $n = 1, 2$ in the quaternionic case, where $S^7$ is a Moufang loop and not a group | *Lie Groups*; *Octonion Representations* |

## The Simple Groups and Their Lie Algebras by Type

A semisimple complex Lie algebra is a direct sum of simple algebras, and the simple algebras correspond to the connected Dynkin diagrams; the rank is the dimension of a Cartan subalgebra and the dimension is $r + \lvert\Phi\rvert$ for the root system $\Phi$. The corresponding compact simply connected groups are the simply connected forms.

| Type | Lie algebra | Rank | Dimension of the algebra | Compact group | Introduced in |
|---|---|---|---|---|---|
| $A_n$ | $\mathfrak{sl}(n+1,\mathbb{C}) = \mathfrak{su}(n+1)$ | $n$ | $n(n+2)$ | $SU(n+1)$ | *Root Systems and Classification*; *Lie Groups* |
| $B_n$ | $\mathfrak{so}(2n+1,\mathbb{C})$ | $n$ | $n(2n+1)$ | $\operatorname{Spin}(2n+1)$ | *Root Systems and Classification*; *The Orthogonal Lie Algebra* |
| $C_n$ | $\mathfrak{sp}(2n,\mathbb{C})$ | $n$ | $n(2n+1)$ | $Sp(n)$ | *Root Systems and Classification* |
| $D_n$ | $\mathfrak{so}(2n,\mathbb{C})$ | $n$ | $n(2n-1)$ | $\operatorname{Spin}(2n)$ | *Root Systems and Classification*; *The Orthogonal Lie Algebra* |
| $G_2$ | $\mathfrak{g}_2 = \operatorname{Der}(\mathbb{O})$ | $2$ | $14$ | $G_2 = \operatorname{Aut}(\mathbb{O})$ | *Root Systems and Classification*; *Octonions and the Exceptional Lie Groups* |
| $F_4$ | $\mathfrak{f}_4$ | $4$ | $52$ | $F_4 = \operatorname{Aut}(\mathfrak{h}_3(\mathbb{O}))$ | *Root Systems and Classification*; *Octonions and the Exceptional Lie Groups* |
| $E_6$ | $\mathfrak{e}_6$ | $6$ | $78$ | the simply connected compact $E_6$ | *Root Systems and Classification*; *Octonions and the Exceptional Lie Groups* |
| $E_7$ | $\mathfrak{e}_7$ | $7$ | $133$ | the simply connected compact $E_7$ | *Root Systems and Classification*; *Octonions and the Exceptional Lie Groups* |
| $E_8$ | $\mathfrak{e}_8$ | $8$ | $248$ | the simply connected compact $E_8$ | *Root Systems and Classification*; *Octonions and the Exceptional Lie Groups* |

The low-dimensional coincidences of the classification are recorded with it: $B_2 = C_2$ and $A_3 = D_3$, and $A_1 = B_1 = C_1$; on the group side, $Sp(1) \cong SU(2)$, $Sp(2,\mathbb{R}) \cong SL_2(\mathbb{R})$, and $\mathfrak{so}(3,1) \cong \mathfrak{sl}_2(\mathbb{C})$ as complex algebras.

## The Correspondence Between a Lie Group and Its Lie Algebra

The passage from the group to the algebra is a functor, and its failure to be an equivalence is measured by the fundamental group of the group; the passage back is the content of Lie's third theorem.

| Object or theorem | The statement or the structure | Introduced in |
|---|---|---|
| the Lie algebra $\mathfrak{g} = T_eG$ | the tangent space at the identity, with the bracket of left-invariant vector fields; $[X,Y] = XY - YX$ for a matrix group | *Lie Groups*; *The Lie Algebra and the Exponential Map* |
| the exponential map $\exp : \mathfrak{g} \to G$ | the flow of a left-invariant field; a local diffeomorphism at $0$, natural in homomorphisms | *The Lie Algebra and the Exponential Map* |
| the Campbell–Baker–Hausdorff formula | $\exp(X)\exp(Y) = \exp(Z(X,Y))$ with $Z$ a Lie polynomial; the group law in exponential coordinates | *The Lie Algebra and the Exponential Map* |
| the differential $d\varphi_e$ | the functor on homomorphisms; a Lie algebra homomorphism | *Lie Groups*; *The Lie Correspondence and the Adjoint Representation* |
| Lie's third theorem | every finite-dimensional real Lie algebra is the Lie algebra of a simply connected Lie group | *The Lie Correspondence and the Adjoint Representation* |
| the Lie correspondence | for simply connected $G$, $\varphi \mapsto d\varphi_e$ is a bijection from $\operatorname{Hom}(G,H)$ to $\operatorname{Hom}(\mathfrak{g},\mathfrak{h})$ | *The Lie Correspondence and the Adjoint Representation* |
| the simply connected cover | $\pi : \tilde G \to G$ with discrete central kernel; the connected groups with a given algebra are the $\tilde G/D$ | *The Lie Correspondence and the Adjoint Representation*; *The Fundamental Group of a Lie Group* |
| the adjoint representation | $\operatorname{Ad}(g) = d(c_g)_e$ on $\mathfrak{g}$ and $\operatorname{ad}_x(y) = [x,y]$, with $d(\operatorname{Ad})_e = \operatorname{ad}$ | *The Lie Correspondence and the Adjoint Representation* |
| the centre | $\ker\operatorname{Ad} = Z(G)$ for connected $G$, and $\operatorname{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g})$ | *The Lie Correspondence and the Adjoint Representation* |
| closed subgroups and quotients | Cartan's theorem makes a closed subgroup embedded; a closed normal $N$ gives $\operatorname{Lie}(G/N) = \mathfrak{g}/\mathfrak{n}$ | *Lie Groups* |
| the structure theory of the algebra | radical, nilradical, Killing form, Cartan's criteria, Levi decomposition, Weyl's complete reducibility | *Structure of Lie Algebras* |
| the highest-weight classification | the irreducible representations of a semisimple algebra by their highest weights | *Representations of Lie Algebras* |
| the Peter–Weyl theorem | the decomposition of $L^2(K)$ for a compact group $K$ into finite-dimensional irreducible representations | *The Peter–Weyl Theorem* |

## Non-examples and Warnings

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| the sphere $S^7$ | it is not a Lie group; among the spheres only $S^0$, $S^1$ and $S^3$ admit a Lie group structure | *Lie Groups* |
| the irrational line in $T^2$ | it is a subgroup of a Lie group and is not a Lie subgroup; its closure is all of $T^2$ and it carries no manifold structure making the inclusion an immersion | *Lie Groups* |
| a quotient $G/H$ by a non-closed subgroup | the quotient is not a manifold; closedness is essential for the homogeneous space to be a Lie group or manifold | *Lie Groups* |
| the exponential map of $SL_2(\mathbb{R})$ | it is not surjective; the image omits the matrices with negative eigenvalue and two distinct real eigenvalues | *Lie Groups*; *The Lie Algebra and the Exponential Map* |
| the Lie functor | it is neither full nor faithful; it sees only the local structure, and the global form needs simple connectivity | *The Lie Correspondence and the Adjoint Representation* |
| the matrix group of a disconnected group | a homomorphism from a disconnected source is not determined by its differential at the identity | *The Lie Correspondence and the Adjoint Representation* |
| $O(n)$, $U(n)$ as group-layer objects | they are *defined* by a form, so they are introduced among the classical geometric groups and are listed here only as matrix Lie groups | *List of Classical Geometric Groups* |

Objects that a reader may expect in a list of Lie groups, and does not find here.

| Object | Why it is not listed here | Introduced in |
|---|---|---|
| infinite-dimensional Lie groups | the corpus treats them with Hilbert's fifth problem and the infinite-dimensional theory; they have no dimension in the finite sense and no Lie correspondence of the same kind | *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory* |
| $p$-adic Lie groups | analytic manifolds over $\mathbb{Q}_p$; they belong to the topological groups list | *$p$-adic Lie Groups*; *List of Topological Groups* |
| algebraic groups and group schemes | defined over a general field, without a smooth manifold structure | *Linear Algebraic Groups*; *Schemes* |
| the Lorentz group's covering group $SL_2(\mathbb{C})$ | it is a matrix Lie group and is recorded with the classical groups; the geometric Lorentz group is recorded with the isometry groups | *Lie Groups*; *List of Isometry and Symmetry Groups* |
| $\operatorname{Spin}(n)$ as a Clifford-algebra object | the spin groups are constructed from the Clifford algebra and are listed with it | *List of Clifford Algebras and Spin Groups* |

## Summary

This article has listed the Lie groups of the corpus with their Lie algebras, dimensions and ranks: the classical matrix groups $GL_n$, $SL_n$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$, $Sp(n)$ and $Sp(2n,\mathbb{R})$; the abelian, nilpotent and semidirect examples, the torus, the Heisenberg group, the Euclidean and affine groups and the Lorentz group; the simple groups and their algebras by type $A_n$, $B_n$, $C_n$, $D_n$, $G_2$, $F_4$, $E_6$, $E_7$, $E_8$, with their ranks and dimensions; and the correspondence between a group and its algebra, the exponential map, the Campbell–Baker–Hausdorff formula, Lie's third theorem, the simply connected cover, the adjoint representation and the structure theory of the algebra. Beside the examples stand the non-examples: $S^7$, the irrational line of the torus, the quotient by a non-closed subgroup, the exponential map of $SL_2(\mathbb{R})$ and the failures of the global correspondence. The list introduces and proves nothing; it is the index of the Lie theory of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $G$, $H$, $\tilde G$ | a Lie group, a second Lie group, the simply connected cover |
| $\mathfrak{g} = T_eG$, $\mathfrak{h}$ | the Lie algebra of $G$, the Lie algebra of $H$; lowercase fraktur throughout |
| $\exp : \mathfrak{g} \to G$ | the exponential map |
| $[X,Y]$, $\operatorname{ad}_x$, $\operatorname{Ad}(g)$ | the bracket, the adjoint representation of the algebra, of the group |
| $d\varphi_e$ | the differential of a homomorphism at the identity |
| $\mathfrak{sl}_n$, $\mathfrak{so}_n$, $\mathfrak{sp}_n$, $\mathfrak{g}_2$, $\mathfrak{f}_4$, $\mathfrak{e}_6$, $\mathfrak{e}_7$, $\mathfrak{e}_8$ | the simple Lie algebras by type |
| $A_n$, $B_n$, $C_n$, $D_n$, $G_2$, $F_4$, $E_6$, $E_7$, $E_8$ | the types of the classification, with $r$ the rank and $\Phi$ the root system |
| $GL_n(\mathbb{K})$, $SL_n(\mathbb{K})$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$, $Sp(n)$, $Sp(2n,\mathbb{R})$ | the classical matrix groups |
| $T^n = U(1)^n$ | the maximal torus of the compact examples |
| $\operatorname{Spin}(n)$ | the universal cover of $SO(n)$ for $n \geq 3$ |
| $Z(G)$, $\mathfrak{z}(\mathfrak{g})$ | the centre of a group and of an algebra |
| $\kappa$ | the Killing form |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Lie group and Lie algebra correspondence and the classical groups.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for Lie's third theorem, the correspondence of categories and the exponential map.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed. 2002), for the structure and classification of the simple groups and their representations.
- John Frank Adams, *Lectures on Exceptional Lie Groups* (University of Chicago Press, 1996), for the construction and properties of $G_2$, $F_4$, $E_6$, $E_7$ and $E_8$.
