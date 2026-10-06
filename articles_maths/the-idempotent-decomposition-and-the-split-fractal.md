# __The Idempotent Decomposition and the Split Fractal__

## Introduction

The biquaternion algebra is simple, so its only central idempotents are $0$ and $e_0$; its non-central idempotents are nevertheless the algebraic form of the splitting of an element into two halves, and the halving is what turns a part of the biquaternion dynamics into a product of two complex dynamics. The decomposition is the Peirce decomposition of the algebra with respect to a primitive idempotent: the space splits into four Peirce components, the two diagonal components are the two halves, and the two off-diagonal components couple them. On the two-dimensional complex subalgebra spanned by the idempotent and its complement the two halves are independent, the map splits into two ordinary complex quadratic maps, and the fractal is the product of two complex Julia sets; off that subalgebra the halves interact and the fractal is not a product.

The idempotents, their classification and the bijection with the roots of $-1$ are *Biquaternion Idempotents and Projections*; the ideals, the Peirce decomposition and the minimal left ideals are *Biquaternion Ideals and Peirce Decomposition*; the matrix model and the rank-one elements are *Biquaternion 2×2 Matrix Element Representation*; the commutative-plane theorem is *The Biquaternion Mandelbrot Set and the Connectedness Locus*; the exact slices are *The Slices of the Biquaternion Julia Sets*; the simplification by central idempotents is *The Clifford Decomposition of the Split-Biquaternion Fractals* on the split side.

The article owns the Peirce decomposition of an element, the identification of the two halves, the diagonal model in which the halves are the two entries of a diagonal matrix, the split fractal and its product structure, and the statement that the full biquaternion fractal is not the product.

**Standing convention.** $\tilde\Pi$ is a primitive idempotent, $\tilde\Pi'=e_0-\tilde\Pi$ its complement, and the four Peirce components of an element $\tilde Q$ are

$$
\tilde Q_{11}=\tilde\Pi\tilde Q\tilde\Pi,\quad \tilde Q_{12}=\tilde\Pi\tilde Q\tilde\Pi',\quad \tilde Q_{21}=\tilde\Pi'\tilde Q\tilde\Pi,\quad \tilde Q_{22}=\tilde\Pi'\tilde Q\tilde\Pi',
$$

so that $\tilde Q=\tilde Q_{11}+\tilde Q_{12}+\tilde Q_{21}+\tilde Q_{22}$. The family is $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$.

## The Peirce Components and the Halves

**Proposition (the components are the matrix entries).** Under the matrix realization with the standard idempotents $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_2=\tfrac12(e_0-ie_3)$,

$$
\Phi(\tilde\Pi_1)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad \Phi(\tilde\Pi_2)=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

and the four Peirce components of $\tilde Q$ with respect to $\tilde\Pi_1$ are the four entries of $\Phi(\tilde Q)$,

$$
\Phi(\tilde Q)=\begin{pmatrix}\Phi(\tilde Q_{11})&\Phi(\tilde Q_{12})\\ \Phi(\tilde Q_{21})&\Phi(\tilde Q_{22})\end{pmatrix} .
$$

**Proof.** The images of the standard idempotents are computed from $\Phi(e_3)=\left(\begin{smallmatrix}-i&0\\0&i\end{smallmatrix}\right)$: the matrix $\Phi(\tfrac12(e_0+ie_3))=\tfrac12\left(\begin{smallmatrix}1+1&0\\0&1-1\end{smallmatrix}\right)$ is the first matrix unit, and the second is its complement. Then $\Phi(\tilde\Pi\tilde Q\tilde\Pi')$ is the product of the corresponding matrix units, which is the off-diagonal entry.

**Corollary (the two halves and the two couplings).** The elements of the form $A\tilde\Pi+B\tilde\Pi'$ have diagonal matrices $\operatorname{diag}(A,B)$; the elements of the form $A\tilde\Pi+B\tilde\Pi'$ together with the two off-diagonal components describe the generic element. **The two halves are the two diagonal entries; the coupling is the pair of off-diagonal entries.**

## The Split Subalgebra and Its Fractal

**Theorem (the split fractal).** Let $\tilde C=C_1\tilde\Pi+C_2\tilde\Pi'$ be a parameter in the idempotent plane $W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$. Then $W_{\tilde\Pi}$ is a commutative subalgebra isomorphic to $\mathbb{C}\oplus\mathbb{C}$, the restriction of $F_{\tilde C}$ to it is

$$
A\tilde\Pi+B\tilde\Pi'\longmapsto(A^2+C_1)\tilde\Pi+(B^2+C_2)\tilde\Pi',
$$

and the restriction of the filled Julia set and the Julia set to the plane are

$$
\mathcal K_{\tilde C}\cap W_{\tilde\Pi}=\bigl(K_{C_1}\tilde\Pi\bigr)\oplus\bigl(K_{C_2}\tilde\Pi'\bigr), \qquad J_{\tilde C}\cap W_{\tilde\Pi}=\partial\bigl(K_{C_1}\times K_{C_2}\bigr),
$$

the product of two complex filled Julia sets. The **split fractal** is this product, and it is the fractal of the diagonal model.

**Proof.** $\tilde\Pi^2=\tilde\Pi$, $\tilde\Pi'^2=\tilde\Pi'$, $\tilde\Pi\tilde\Pi'=0$ give the coordinatewise product and the split map; the two coordinates do not interact, so the orbit is the pair of complex orbits and the locus is the product. The boundary formula is the boundary of a product.

**Remark (the diagonal model).** In the model the split fractal is the set of diagonal matrices $\operatorname{diag}(\lambda_1,\lambda_2)$ with $\lambda_j$ in the complex filled Julia set $K_{C_j}$; the parameter is the diagonal matrix $\operatorname{diag}(C_1,C_2)$ and the map is the entrywise square plus the parameter. **The diagonal matrices carry exactly the product of two complex quadratic dynamics, and they are the largest subalgebra on which the biquaternion dynamics is a product.** The off-diagonal entries are zero on the plane and are the coupling off it.

## The Coupling and the Failure of the Product

**Proposition (the entries of the square).** With the entry notation $\Phi(\tilde Q)=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$,

$$
\Phi(\tilde Q^2)=\begin{pmatrix}a^2+bc & b(a+d)\\ c(a+d) & cb+d^2\end{pmatrix} .
$$

Hence the two diagonal entries evolve by $a\mapsto a^2+bc$ and $d\mapsto cb+d^2$, with the off-diagonal product $bc$ appearing as a parameter; the two off-diagonal entries evolve by the multiplication by the trace $a+d$; and the coupling is exactly the trace times the off-diagonal pair.

**Proof.** Direct multiplication of two two-by-two matrices.

**Theorem (the product description is exactly the plane).** The idempotent plane is invariant under $F_{\tilde C}$ if and only if $\tilde C\in W_{\tilde\Pi}$, and in that case the Julia set restricted to the plane is the boundary of $K_{C_1}\times K_{C_2}$. If $\tilde C\notin W_{\tilde\Pi}$ the plane is not invariant and no product $J_{C_1}\times J_{C_2}$ of two complex Julia sets describes $J_{\tilde C}$: the two halves are coupled through the trace and the off-diagonal product.

**Proof.** $F_{\tilde C}(W_{\tilde\Pi})\subset W_{\tilde\Pi}$ requires the off-diagonal entries of $\tilde C$ to vanish, i.e. $\tilde C\in W_{\tilde\Pi}$; for such a parameter the set is the product by the theorem above. For any other parameter the plane is not invariant, and the entry formula of the previous proposition exhibits the coupling: the diagonal entries of $\Phi(\tilde Q^2)$ contain the off-diagonal product $bc$ and the off-diagonal entries contain the trace $a+d$, so the two halves are not independent and their orbits are not the orbits of a pair of one-variable maps. A set that is a product of two one-variable Julia sets would give independent halves, and no such description is available.

**Remark (the reconstruction is obstructed).** The pair of halves is not enough to determine the orbit, because the coupling term $bc$ enters the diagonal dynamics; the reconstruction of the biquaternion fractal from the split fractal therefore fails, and the failure is quantitative: the coupling is bilinear in the off-diagonal entries and can be small in a slice and large in the fractal. **The split fractal is an exact slice and not a decomposition.**

## The Split-Biquaternion Contrast

**Proposition (the centrality of the split idempotents).** In the split-biquaternion algebra the idempotents

$$
\tilde\Pi_\pm=\tfrac12(e_0\pm j)
$$

are **central**, $j$ being the central element with $j^2=1$, and the algebra factors as the direct sum of two ideals,

$$
\mathbb{H}_{\mathbb{D}}=\mathbb{H}\tilde\Pi_+\oplus\mathbb{H}\tilde\Pi_- , \qquad \mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H},
$$

through central idempotents, so that the decomposition is one of the algebra and of every element and splits the dynamics globally, not on a slice. Then every quadratic map is the pair of two quaternion quadratic maps, the fractal is the product of two quaternion Julia sets, and there is no coupling term. **The biquaternion case is the case of non-central idempotents: the splitting is real but local; the split-biquaternion case is the case of central idempotents: the splitting is global.** The contrast is developed in *The Clifford Decomposition of the Split-Biquaternion Fractals*.

**Proof.** $j$ is central with $j^2=1$, so $\tilde\Pi_\pm$ are central idempotents with $\tilde\Pi_++\tilde\Pi_-=e_0$ and $\tilde\Pi_+\tilde\Pi_-=0$; the Chinese-remainder decomposition of the algebra follows. In $\mathbb{B}$, by contrast, no non-trivial central idempotent exists because the algebra is simple (*Biquaternion Ideals and Peirce Decomposition*).

## Summary

The Peirce decomposition of a biquaternion with respect to a primitive idempotent has four components, which in the matrix model are exactly the four entries of the matrix; the two diagonal components are the halves of the element and the two off-diagonal ones are the coupling. On the idempotent plane the map splits into two independent complex quadratic maps, the filled Julia set is the product of two complex filled Julia sets and the split fractal is that product; the plane is the largest subalgebra on which the dynamics is a product. Off the plane the entries of the square show the coupling: the diagonal entries evolve with the off-diagonal product as a parameter, the off-diagonal entries are multiplied by the trace, and the full fractal is strictly larger than its diagonal slices and not a product. The contrast with the split-biquaternion algebra is sharp: there the idempotents are central, the algebra factors globally, and the fractal is a product of two quaternion Julia sets with no coupling at all.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi$, $\tilde\Pi'=e_0-\tilde\Pi$ | a primitive idempotent and its complement |
| $\tilde\Pi_1,\tilde\Pi_2$ | the standard idempotents $\tfrac12(e_0\pm ie_3)$ |
| $\tilde Q_{11},\tilde Q_{12},\tilde Q_{21},\tilde Q_{22}$ | the four Peirce components |
| $W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$ | the idempotent plane |
| $K_{C_1}\times K_{C_2}$ | the split fractal, a product of complex filled Julia sets |
| $a,b,c,d$ | the four matrix entries |
| $a+d$ | the trace, the coupling multiplier |
| $\tilde\Pi_\pm=\tfrac12(e_0\pm j)$ | the central idempotents of the split-biquaternion algebra |

## Further Reading

- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents, their classification and the standard pair.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the ideals and the Peirce decomposition used here.
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the matrix model and the identification of the components with the entries.
- *The Slices of the Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-biquaternion-julia-sets.md`), for the placement of the split fractal among the slices.
- *The Clifford Decomposition of the Split-Biquaternion Fractals* (`articles_maths/the-clifford-decomposition-of-the-split-biquaternion-fractals.md`), for the central-idempotent contrast.
