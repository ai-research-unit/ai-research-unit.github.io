
# __List of Geometric Lattices and Integral Forms__

## Introduction

This article lists the lattices of the corpus, their covolumes, their duals and the integral forms they carry, from the elementary lattice $\mathbb{Z}^n$ to the Lipschitz and Hurwitz lattices of the quaternion algebra. Every entry points to the article that introduces the lattice or the form, and the article introduces nothing and proves nothing.

A lattice is a free abelian group of finite rank with an embedding in a real vector space, and the data that classify it geometrically are its Gram matrix, its covolume and its dual with respect to a form. The list gathers the abstract lattices as free $\mathbb{Z}$-modules, the Euclidean lattices and their covolumes, the dual lattices and the discriminants, the integral quadratic and bilinear forms that a lattice carries, the lattices of the ring of integers of a number field, and the two quaternion orders of the corpus, the Lipschitz and the Hurwitz lattice. The lattice in the sense of a discrete subgroup of finite covolume in a Lie group is a different object, and it is recorded in the warnings with the article that treats it.

The article records examples and non-examples side by side. Beside the lattices it lists the dense subgroups that fail discreteness, the sets that are not finitely generated, the lattices that are not free, and the second sense in which the corpus uses the word lattice, each with the failure named and the article that records it.

## Lattices as Free $\mathbb{Z}$-Modules

A lattice is a free abelian group of finite rank, and its rank, its sublattices and its indices are the algebraic data on which the geometry is built.

| Object | The property it has | Introduced in |
|---|---|---|
| a lattice $\Lambda$ | a free $\mathbb{Z}$-module of finite rank $n$ | *Lattices and the Quaternion Lattice* |
| the rank $n$ | the number of generators, the dimension of the ambient space | *Lattices and the Quaternion Lattice* |
| the change-of-basis matrix $A$ | the matrix relating two bases, of determinant equal to the index | *Lattices and the Quaternion Lattice* |
| a sublattice $\Lambda' \leq \Lambda$ | a free submodule of the same rank, of finite index in the geometric case | *Lattices and the Quaternion Lattice* |
| the index $[\Lambda:\Lambda']$ | the determinant of the change of basis, the ratio of the covolumes | *Lattices and the Quaternion Lattice* |
| the free $\mathbb{Z}$-module of rank $n$ | the abstract lattice, without an embedding | *Direct Sums, Free Modules and Rank* |
| the elementary lattice $\mathbb{Z}^n \leq \mathbb{R}^n$ | the standard lattice, a rank-$n$ subgroup with covolume $1$ | *Lattices in Lie Groups* |
| the period lattice $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ | the rank-two lattice of the periods of the elliptic functions, on which $\mathbb{C}/\Lambda$ is an elliptic curve | *Elliptic Functions and Integrals* (planned) |

The lattice is a free module, so it has a basis, and a sublattice of finite index has a basis whose change-of-basis matrix has determinant equal to the index. The elementary lattice and its images by invertible linear maps are the Euclidean lattices, and the abstract free module is the algebraic object from which they are obtained by a choice of embedding.

## The Euclidean Lattice and its Covolume

An embedded lattice has a Gram matrix, and the square root of its determinant is the covolume, the volume of a fundamental domain.

| Object | The property it has | Introduced in |
|---|---|---|
| the Gram matrix $G = (v_i\cdot v_j)$ | the matrix of the inner products of a basis, encoding the metric of the lattice | *Lattices and the Quaternion Lattice* |
| the covolume $\operatorname{covol}(\Lambda) = \sqrt{\det G}$ | the volume of a fundamental domain, the density of the embedding | *Lattices and the Quaternion Lattice* |
| the scaling law $\operatorname{covol}(\Lambda') = [\Lambda:\Lambda']\operatorname{covol}(\Lambda)$ | the index times the covolume is the covolume | *Lattices and the Quaternion Lattice* |
| the lattice $A\mathbb{Z}^n$ in $\mathbb{R}^n$ | a lattice of covolume $\lvert\det A\rvert$ | *Lattices in Lie Groups* |
| the integral lattice | a lattice with a positive-definite integral Gram matrix | *Lattices and the Quaternion Lattice* |
| the covolume of the arithmetic quotient | the volume $\mu(G/\Gamma)$ of a lattice in a Lie group, defined up to normalisation | *Lattices in Lie Groups* |

The Gram matrix is the complete metric data of the lattice, and the covolume is its geometric size: it is the volume of the parallelotope spanned by a basis, and it multiplies by the index under the passage to a sublattice. The covolume of a lattice in a Lie group is the volume of the quotient, and it is the invariant by which the arithmetic lattices are compared; the two covolumes share the name and the scaling property, though the objects are different.

## The Dual Lattice and the Discriminant of the Form

The dual lattice is the set of vectors whose inner products with the lattice are integral, and the discriminant of the form together with the order of the quotient $\Lambda^*/\Lambda$ measures the embedding of the lattice in its dual.

| Object | The property it has | Introduced in |
|---|---|---|
| the dual lattice $\Lambda^*$ | the vectors $y$ with $x\cdot y \in \mathbb{Z}$ for all $x \in \Lambda$ | *Lattices and the Quaternion Lattice* |
| the discriminant of the form | the determinant of the Gram matrix up to squares, an invariant of the isometry class | *Bilinear Forms*, §Congruence and the Discriminant |
| the integrality of the norm form | the norm $N(x) = x\bar x$ is integer-valued on the Lipschitz and the Hurwitz lattice | *Lattices and the Quaternion Lattice* |
| the discriminant $d_K$ of a number field | the determinant of an integral basis of $\mathcal{O}_K$ | *Algebraic Number Theory* |
| the ring of integers $\mathcal{O}_K$ | a lattice of rank $n = [K:\mathbb{Q}]$, with an integral basis | *Algebraic Number Theory* |

The dual lattice sits between the lattice and its real span, the quotient $\Lambda^*/\Lambda$ is the finite group that measures the failure of the lattice to be self-dual, of order four for the Hurwitz lattice, For the ring of integers the discriminant is the arithmetic invariant of the number field, and the ramified primes are exactly its prime divisors.

## Integral Forms

An integral form is a bilinear or quadratic form taking integral values on a lattice, and the form is the datum that makes the lattice a geometric object.

| Object | The property it has | Introduced in |
|---|---|---|
| an integral quadratic form | a quadratic form $q$ with $q(x) \in \mathbb{Z}$ for all lattice vectors | *Quadratic Forms and Polarisation* |
| the polar form $g(u,v) = \tfrac12(q(u+v)-q(u)-q(v))$ | the bilinear form associated with a quadratic form | *Quadratic Forms and Polarisation* |
| an integral bilinear form | a symmetric bilinear form with integral values on the lattice | *Bilinear Forms* |
| the Gram matrix of a form | the matrix of an integral form, an integral matrix | *Bilinear Forms* |
| the norm form $N(x) = x\bar x$ | the quadratic form of the quaternion algebra, integral on the quaternion lattices | *Lattices and the Quaternion Lattice* |
| the polar form $(x,y) = \operatorname{Sc}(x\bar y)$ | the Euclidean dot product, the polar form of the norm | *Lattices and the Quaternion Lattice* |
| the radical of an integral form | the vectors orthogonal to the whole space, the obstruction to nondegeneracy | *Bilinear Forms*, §Rank and the Radical |

The passage from an integral form to a lattice and back is the arithmetic content of the geometry: the Gram matrix of a basis is the matrix of the form, the covolume is its determinant, the dual lattice is the lattice of the inverse form, and the integrality of the form is the condition $\Lambda\subseteq\Lambda^*$. The norm form of the quaternion algebra is the classical example of an integral quaternary form, and its polar form is the Euclidean dot product.

## The Quaternion Lattices

The Lipschitz and Hurwitz lattices are the integral forms of the quaternion algebra, and the Hurwitz lattice is the maximal order.

| Object | The property it has | Introduced in |
|---|---|---|
| the Lipschitz lattice $\mathbb{H}(\mathbb{Z})$ | the integer span of the quaternion basis, rank $4$, not maximal | *Lattices and the Quaternion Lattice* |
| the Hurwitz lattice $\mathbb{H}'(\mathbb{Z})$ | the order with the half-integral generator $\omega = \tfrac12(1+e_1+e_2+e_3)$, rank $4$, maximal | *Lattices and the Quaternion Lattice* |
| the Hurwitz unit group | the $24$ units of the Hurwitz order, the binary tetrahedral group $2T$ | *Quaternion Geometry*, §The Units and Their Geometry |
| the norm form on the lattice | the sum of four squares, the integral quadratic form of the lattice | *Quaternion Geometry*, §The Arithmetic Geometry of the Quaternion Lattice |
| the unit sphere lattice | the unit sphere carries a discrete subgroup of finite covolume, up to scaling | *Quaternion Geometry*, §The Units and Their Geometry |

The Hurwitz order contains the Lipschitz order with index two, and it is the maximal order of the rational quaternion algebra; the unit group is finite of order $24$ and is the binary tetrahedral group. The lattice is the arithmetic counterpart of the geometry of the quaternion sphere, and the norm form is the quaternary quadratic form that the lattice carries.

## Warnings

An object that a reader may expect among the geometric lattices and integral forms, and does not find, is recorded with the reason.

| Object | Why it is not listed as a geometric lattice | Introduced in |
|---|---|---|
| a lattice in a Lie group | a discrete subgroup of finite covolume, a different sense of the word, treated with the discrete geometric groups | *Lattices in Lie Groups* |
| a non-uniform lattice | finite covolume but noncompact quotient, with cusps; it is a lattice in the Lie-group sense | *Lattices in Lie Groups* |
| a dense subgroup of $\mathbb{R}^n$ | not discrete, so not a lattice in any sense | *Topological Groups* |
| the rational lattice $\mathbb{Q}^n$ | not discrete and not finitely generated over $\mathbb{Z}$ | *Direct Sums, Free Modules and Rank* |
| the dual of a lattice with no form fixed | the dual depends on the form; without one the construction is undefined | *Lattices and the Quaternion Lattice* |

## Summary

This article has listed the geometric lattices and integral forms of the corpus. The lattices as free $\mathbb{Z}$-modules open the list, with their rank, their sublattices and their indices; the Euclidean lattices follow, with the Gram matrix and the covolume, together with the covolume of a lattice in a Lie group; the dual lattice, the discriminant and the ring of integers of a number field are recorded; the integral quadratic and bilinear forms are gathered with the polar form, the norm form and the radical; and the Lipschitz and Hurwitz lattices close the list with the norm form and the Hurwitz unit group. Beside the examples stand the non-examples: a dense subgroup is not discrete, the rational lattice is not finitely generated, the dual is undefined without a form, and a lattice in a Lie group is a lattice in the other sense of the word.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\Lambda$, $\Lambda^*$, $n$, $[\Lambda:\Lambda']$ | Lattice, dual, rank, index |
| $G = (v_i\cdot v_j)$, $\operatorname{covol}(\Lambda) = \sqrt{\det G}$ | Gram matrix and covolume |
| $\mathbb{Z}^n$, $A\mathbb{Z}^n$ | Elementary lattice and its linear images |
| $\mathcal{O}_K$, $d_K$ | Ring of integers and discriminant of a number field |
| $q$, $g(u,v)$, $N(x) = x\bar x$ | Quadratic form, polar form, quaternion norm form |
| $\mathbb{H}(\mathbb{Z})$, $\mathbb{H}'(\mathbb{Z})$ | Lipschitz lattice, Hurwitz lattice |
| $\omega = \tfrac12(1+e_1+e_2+e_3)$ | Half-integral generator of the Hurwitz order |
| $\mu(G/\Gamma)$, $\operatorname{covol}(\Gamma)$ | Haar measure and covolume of a lattice in a Lie group |
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The standard number systems of the corpus |
| $\operatorname{Sc}(x)$ | The scalar part of a quaternion product |

## Further Reading

- John Horton Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for the lattices, their covolumes, their duals and the integral forms.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the integral quadratic forms and the four-square theorem.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the Lipschitz and Hurwitz orders and their arithmetic.
- J. W. S. Cassels, *An Introduction to the Geometry of Numbers* (Springer, 1959), for the covolume, the fundamental domain and the Minkowski theory of the Euclidean lattices.
