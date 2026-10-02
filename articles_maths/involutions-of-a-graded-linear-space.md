# __Involutions of a Graded Linear Space__

## Introduction

A $\mathbb{Z}/2$-grading of a linear space is a decomposition $V = V_0 \oplus V_1$, and the involution it defines is the map that acts as $+\mathrm{id}$ on the even part $V_0$ and as $-\mathrm{id}$ on the odd part $V_1$; it is the **grade involution**. This article is about that involution and about the equivalence that makes it more than an example: a linear involution and a $\mathbb{Z}/2$-grading are the same datum read in two ways, the grading selected by an involution being the decomposition into its fixed and negated parts and the involution selected by a grading being the grade involution. With the grading come the parity of vectors and of endomorphisms, the decomposition of the endomorphism algebra into its even and odd parts, and the graded dual and graded tensor product, on which the grade involution propagates.

The general linear involution, its type $(p,q)$, its trace $p-q$, its determinant $(-1)^{q}$, the conjugacy classification and the collapse in characteristic two are *Involutive Linear Spaces*, and the present article is a companion inside the same `*`-theory group: it fixes the graded reading and the parity vocabulary that the graded operator articles use. The general theory of superalgebras, the graded tensor product of algebras and the **sign rule** $\tau = -\mathrm{id}$ on the odd-odd part of a tensor square belong to *Superalgebras and Graded Structures*, written in this Part, and they are named here only to mark the boundary and are not used. The transposed involution on the dual is *Involutions of the Dual Space*, and the involution on the endomorphism algebra from a pairing is *Involutions of the Endomorphism Algebra*.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, a **grading** is a direct decomposition $V = V_0 \oplus V_1$ with $V_0,V_1$ subspaces, and a vector is **even** when it lies in $V_0$ and **odd** when it lies in $V_1$. No form, no norm and no topology is used.

## The Grading and the Grade Involution

**Definition.** A **graded linear space** is a pair $(V, V_0, V_1)$ with $V = V_0 \oplus V_1$. The **grade involution** is the linear map

$$
\alpha : V \longrightarrow V, \qquad \alpha(v_0 + v_1) = v_0 - v_1 \quad (v_0 \in V_0,\ v_1 \in V_1) .
$$

**Proposition (the grade involution is an involution).** $\alpha$ is a linear involution of $V$, of type $(\dim_F V_0, \dim_F V_1)$, with the projectors

$$
P_0 = \tfrac12(\mathrm{id}+\alpha), \qquad P_1 = \tfrac12(\mathrm{id}-\alpha)
$$

onto the two parts. Conversely, for every linear involution $T$ of $V$ the decomposition

$$
V_0 = \ker(T-\mathrm{id}) = V_+, \qquad V_1 = \ker(T+\mathrm{id}) = V_-
$$

is a grading, and the grade involution of that grading is $T$ itself.

**Proof.** Linearity of $\alpha$ is the definition; $\alpha^2 = \mathrm{id}$ because $\alpha$ fixes $V_0$ and negates $V_1$; the fixed part is $V_0$ and the negated part is $V_1$, so the type is $(\dim V_0,\dim V_1)$. The projectors satisfy $P_0^2=P_0$, $\operatorname{im}P_0 = V_0$ and $\ker P_0 = V_1$, and similarly for $P_1$. For the converse, the eigenspace decomposition of an involution is a direct sum; the map negating $V_-$ and fixing $V_+$ is exactly $T$.

**Corollary (the two readings are one datum).** The assignment of the grade involution to a grading and the assignment of the grading to a linear involution are inverse bijections between the gradings of $V$ and the linear involutions of $V$. In particular a graded linear space and an involutive linear space are two names for the same object, and every statement about one has a translation into the other.

**Remark (how the two corpora readings differ).** *Involutive Linear Spaces* reads the datum through the operator and classifies it by the type; the graded reading reads the same datum through the parity and is the one the graded operator articles use. The parity is not a new invariant: it is the type $(p,q)$ written as a designation of the two parts.

**Example.** For $V$ of dimension $4$ with $V_0$ of dimension $3$ and $V_1$ of dimension $1$, the grade involution has type $(3,1)$; in a basis adapted to the decomposition its matrix is $\operatorname{diag}(1,1,1,-1)$, of trace $2$ and determinant $-1$. The same matrix read as an involution has fixed part the first three coordinates and negated part the fourth.

## The Parity of Endomorphisms

**Definition.** A linear map $f : V \to W$ of graded spaces is **even** when $f(V_i) \subseteq W_i$ for $i = 0,1$ and **odd** when $f(V_i) \subseteq W_{1-i}$ for $i = 0,1$; a general linear map decomposes uniquely into an even and an odd part.

**Proposition.** For a graded space $V$, every endomorphism $X \in E = \operatorname{End}_F(V)$ is uniquely $X = X_0 + X_1$ with $X_0$ even and $X_1$ odd, and

$$
E = E_0 \oplus E_1 , \qquad E_0 = \{X : \alpha X \alpha = X\} , \qquad E_1 = \{X : \alpha X \alpha = -X\} .
$$

The conjugation $\Phi_\alpha(X) = \alpha X \alpha$ is an involution of the linear space $E$, equal to the grade involution of the grading $E = E_0 \oplus E_1$; its type is $(p^2+q^2, 2pq)$ with $p=\dim V_0$ and $q=\dim V_1$, and its trace is $(p-q)^2$.

**Proof.** The decomposition of a matrix in a basis adapted to $V_0 \oplus V_1$ into its four blocks, and the grouping of the two diagonal blocks as even and the two off-diagonal blocks as odd, gives $E = E_0\oplus E_1$; the condition $\alpha X \alpha = X$ is exactly the preservation of the two parts, and $\alpha X \alpha = -X$ the exchange of them. The assertions about $\Phi_\alpha$ and its type are the computation of *Involutive Linear Spaces* for the involution $T=\alpha$: in the basis of matrix units $E_{ij}$, $\Phi_\alpha(E_{ij}) = \varepsilon_i\varepsilon_j E_{ij}$ with $\varepsilon_i = 1$ for the even indices and $-1$ for the odd ones, so the eigenvalue $1$ occurs $p^2+q^2$ times and $-1$ occurs $2pq$ times.

**Corollary (the multiplication without the sign).** The product of two even endomorphisms and the product of two odd endomorphisms are even, and the product of an even and an odd endomorphism is odd; hence $E_0E_0 \subseteq E_0$, $E_1E_1 \subseteq E_0$, $E_0E_1 \subseteq E_1$ and $E_1E_0 \subseteq E_1$. The **graded commutator** $[X,Y] = XY - (-1)^{|X||Y|}YX$, which uses the sign rule, is *Superalgebras and Graded Structures*, and only the parity of the products is used here.

**Proof.** The block multiplication in the adapted basis; the parity of a product is the sum of the parities of the factors.

## The Graded Dual and the Graded Tensor Product

**Proposition (the graded dual).** The dual of a graded space is graded by

$$
(V^{*})_0 = (V_1)^{0}, \qquad (V^{*})_1 = (V_0)^{0} ,
$$

where the first is the set of functionals vanishing on $V_1$ and the second the set vanishing on $V_0$; equivalently $(V^{*})_i \cong (V_i)^{*}$, and the transposed involution $\alpha^{*}$ is the grade involution of $V^{*}$.

**Proof.** A functional vanishing on $V_1$ is fixed by $\alpha^{*}$, because $\alpha^{*}\varphi = \varphi\alpha$ and $\varphi\alpha = \varphi$ on $V_0$ and vanishes on $V_1$; hence the fixed part of $\alpha^{*}$ is the annihilator of $V_1$, of dimension $p$, and the negated part is the annihilator of $V_0$, of dimension $q$. This is *Involutions of the Dual Space*, and the identifications with $(V_i)^{*}$ are the restriction maps.

**Proposition (the graded tensor product).** For graded spaces $V$ and $W$ the tensor product is graded by

$$
(V\otimes_F W)_0 = (V_0\otimes W_0) \oplus (V_1\otimes W_1), \qquad (V\otimes_F W)_1 = (V_0\otimes W_1) \oplus (V_1\otimes W_0) ,
$$

and the grade involution of the tensor product is $\alpha_V \otimes \alpha_W$.

**Proof.** The tensor product of the decompositions is the direct sum of the four spaces $V_i\otimes W_j$, and $\alpha_V\otimes\alpha_W$ acts on $V_i\otimes W_j$ by $(-1)^{i+j}$, which is $+1$ for the two diagonals and $-1$ for the two off-diagonals.

**Remark (the deferred sign).** On the flip $\tau : V\otimes W \to W\otimes V$ the grading alone gives $\tau^2 = \mathrm{id}$; the assignment $\tau = -\mathrm{id}$ on the odd-odd part, which turns the tensor product of graded algebras into a graded algebra, is the **sign rule** and belongs to *Superalgebras and Graded Structures*. It is named here because the graded operator articles refer to it, and it is not used or defined.

## Summary

A $\mathbb{Z}/2$-grading $V = V_0\oplus V_1$ and a linear involution of $V$ are the same datum: the grade involution $\alpha$, equal to $+\mathrm{id}$ on $V_0$ and $-\mathrm{id}$ on $V_1$, has the grading as its eigenspace decomposition, and the eigenspace decomposition of any linear involution is a grading with that involution as its grade involution. The grade involution has type $(\dim V_0,\dim V_1)$ and projectors $\tfrac12(\mathrm{id}\pm\alpha)$. An endomorphism of a graded space is even or odd according to whether it preserves or exchanges the two parts; the endomorphism algebra decomposes as $E = E_0\oplus E_1$ with $E_0$ the even and $E_1$ the odd endomorphisms, the conjugation $\Phi_\alpha$ being the grade involution of that decomposition, of type $(p^2+q^2,2pq)$ and trace $(p-q)^2$. The dual is graded by the annihilators of the two parts with the transposed involution as grade involution, and the tensor product is graded by the parity of the sum of the parities, with $\alpha_V\otimes\alpha_W$ its grade involution. The sign rule on the flip, and the general theory of superalgebras, are *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars |
| $V = V_0\oplus V_1$ | a graded linear space, $V_0$ even and $V_1$ odd |
| $p,q$ | $p=\dim_F V_0$, $q=\dim_F V_1$ |
| $\alpha$ | the grade involution, $+\mathrm{id}$ on $V_0$, $-\mathrm{id}$ on $V_1$ |
| $P_0,P_1 = \tfrac12(\mathrm{id}\pm\alpha)$ | the projectors onto the two parts |
| $E = \operatorname{End}_F(V)$ | the endomorphism algebra |
| $E_0,E_1$ | the even and odd endomorphisms, $E=E_0\oplus E_1$ |
| $\Phi_\alpha(X)=\alpha X\alpha$ | the grade involution of $E$ |
| $(V^{*})_0,(V^{*})_1$ | the graded parts of the dual |
| $\alpha_V\otimes\alpha_W$ | the grade involution of a tensor product |
| $\tau$ | the flip, whose sign rule is deferred |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for graded vector spaces and gradings of algebras.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the parity conventions of graded linear algebra.
- Nathan Jacobson, *Lectures in Abstract Algebra*, volume II: *Linear Algebra* (Van Nostrand, 1953), for involutions, their eigenspace decompositions and the induced maps on duals and tensor products.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, 2nd ed. 1997), for the linear algebra of graded spaces and the sign rule.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the parity grading and the grade involution of an endomorphism algebra.
