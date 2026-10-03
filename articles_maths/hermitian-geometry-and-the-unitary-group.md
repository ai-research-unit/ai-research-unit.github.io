
# __Hermitian Geometry and the Unitary Group__

## Introduction

A **Hermitian form** on a complex vector space is a sesquilinear form that is conjugate-symmetric, linear in the first argument and conjugate-linear in the second,
$$
h(x, y) = \overline{h(y, x)},
$$
so that the quadratic function $q(x) = h(x, x)$ is real; the form is **positive definite** when $q(x) > 0$ for $x \neq 0$, and the positive-definite Hermitian forms are the inner products of the geometry. The group that preserves such a form is the **unitary group**,
$$
U(h) = \{ g \in GL(V) : h(gx, gy) = h(x, y)\ \text{for all } x, y\},
$$
and in a **unitary frame** — a complex basis $e_1,\dots,e_m$ with $h(e_i,e_j) = \delta_{ij}$ — it is the group of matrices with $A^{\dagger}A = I$, the classical unitary group $U(m)$. The two objects are the two faces of one structure: the Hermitian form is the organ of the chapter, and the unitary group is its isometry group; the Gram matrix of the form is Hermitian and definite, the Sylvester normal form brings the form to $\sum |z_i|^2$ for the definite case and to the difference of two such sums in general, and the signature $(p,q)$ of the indefinite forms is the index that classifies them and their groups $U(p,q)$. The unitary frames are the frames adapted to the form, the Gram–Schmidt process is the algorithm that produces them, and the action of the unitary group on them is transitive, so the geometry of the pair is the geometry of a symmetric space.

The article has three sections: the Hermitian forms and their Gram matrices; the unitary group and the unitary frames; and the geometries the two define, the space of forms and the Grassmannians. The complex structures and the Hermitian metrics are *The Almost Complex Operator*, *Hermitian Geometry and Almost Complex Structures* and *Kähler Manifolds and the Hermitian Form*; the real structure and the linear conjugation are *The Involution on a Complex Vector Space*; the signatures and the real forms of the compatible conjugations are *Complex Manifolds with an Antiholomorphic Involution*; the Hermitian symmetric space and the compact Grassmannian are *Hermitian Symmetric Spaces and the Bergman Metric* and *The Unitary Group and the Hermitian Symmetric Space*; the representations of the unitary group are *Unitary Representations of a Lie Group*. None of that is re-derived.

Throughout, $V$ is a complex vector space of dimension $m$, $h$ is a Hermitian form on $V$, $q(x) = h(x,x)$ its quadratic function, $H$ is the Gram matrix of $h$ in a basis, $U(h)$ is the unitary group of $h$, $U(p,q)$ is the unitary group of the form of signature $(p,q)$ with $p+q=m$, and $U(m) = U(m,0)$.

## The Hermitian Forms and Their Gram Matrices

**Definition.** A **Hermitian form** on $V$ is a map $h : V\times V \to \mathbb{C}$, linear in the first argument and conjugate-linear in the second, with $h(y,x) = \overline{h(x,y)}$; its **Gram matrix** in a basis $e_1,\dots,e_m$ is $H_{ij} = h(e_i,e_j)$, a Hermitian matrix, $H^{\dagger} = H$. The form is **positive definite** when $q(x) = h(x,x) > 0$ for $x\neq0$, **negative definite** when $q(x)<0$, and **indefinite** otherwise.

**Proposition (polarisation).** A Hermitian form is determined by its quadratic function $q(x) = h(x,x)$, through
$$
h(x, y) = \tfrac14 \sum_{k=0}^{3} i^{k}\, q(y + i^{k}x) ,
$$
and $q$ takes real values; conversely a real-valued quadratic function satisfying this polarisation is a Hermitian form.

**Proof.** Expand $q(y+i^kx) = h(y,y) + i^{k}h(y,x) + i^{-k}h(x,y) + h(x,x)$ using the sesquilinearity and the four values $i^k = 1, i, -1, -i$. Weighting by $i^k$ and summing, the terms $h(x,x)$ and $h(y,y)$ contribute $\sum_k i^k = 0$, the cross term $h(y,x)$ contributes $\sum_k i^{2k} = 0$, and the remaining term contributes $\sum_k i^{k}i^{-k} = 4$, leaving $4h(x,y)$. This is *Sesquilinear Forms and the Lax–Milgram Theorem* and *Quadratic Forms and Polarisation*.

**Theorem (Sylvester normal form).** Every Hermitian form on $V$ is equivalent, under a change of basis in $GL(V)$, to the normal form
$$
h(z, w) = \sum_{i=1}^{p} z_i\bar w_i - \sum_{j=p+1}^{m} z_j\bar w_j
$$
for a unique pair $(p,q)$ with $p+q=m$; the pair is the **signature** of the form, the number $p$ is its **index of positivity** and $q$ its **index of negativity**, and the normal form is obtained by the Gram–Schmidt process applied to the form.

**Proof.** The diagonalisation of the Hermitian matrix $H$ by a unitary change of basis gives real eigenvalues; scaling the basis vectors by the positive square roots of the absolute values brings each eigenvalue to $\pm1$, giving the normal form; the uniqueness of the number of positive signs is Sylvester's law of inertia, proved by the maximality of the dimension of a subspace on which the form is positive definite. The diagonalisation of a Hermitian matrix is *Self-Adjoint Operators and the Spectral Theorem*, and the inertia is *Quadratic Forms and Polarisation*.

**Corollary (the associated real form).** Writing $h = g - i\omega$ with $g(x,y) = \operatorname{Re}h(x,y)$ and $\omega(x,y) = -\operatorname{Im}h(x,y)$, the real part $g$ is a symmetric bilinear form on the underlying real space, the imaginary part $\omega$ is alternating, and for a positive-definite $h$ the form $g$ is an inner product and the operator $J$ is a $g$-isometry; the complex structure is skew-adjoint for $h$, $h(Jx,y) = -h(x,Jy)$... equivalently $J^{\dagger} = -J$.

**Proof.** The symmetry of $g$ and the antisymmetry of $\omega$ follow from the conjugate symmetry of $h$ at real and imaginary values; $g$ is positive definite with $h$, and $h(Jx,Jy)=h(x,y)$ is the compatibility of $J$ with the form, so $J$ is an isometry of $g$; the adjoint relation $h(Jx,y)=\overline{h(x,Jy)}=-h(x,Jy)$... follows from the conjugate-linearity in the second argument and $h(Jx,Jy)=h(x,y)$. This is *The Involution on a Complex Vector Space*.

## The Unitary Group and the Unitary Frames

**Definition.** A **unitary frame** of $(V, h)$ is a complex basis $e_1,\dots,e_m$ with $h(e_i,e_j) = \delta_{ij}$; in a unitary frame the Gram matrix of $h$ is the identity, and a **unitary** operator is one preserving $h$, $h(gx, gy) = h(x,y)$.

**Proposition (the unitary group).** The unitary operators of $(V,h)$ form a group $U(h)$, and in a unitary frame the group is
$$
U(h) \cong U(m) = \{ A \in GL(m, \mathbb{C}) : A^{\dagger}A = I \} ,
$$
the classical **unitary group**; the **special unitary group** $SU(m)$ is the subgroup of the unitaries with $\det A = 1$, and every unitary has $|\det A| = 1$. For the indefinite form of signature $(p,q)$ in a normal frame the group is
$$
U(p,q) = \{ A : A^{\dagger} I_{p,q} A = I_{p,q}\}, \qquad I_{p,q} = \operatorname{diag}(1,\dots,1,-1,\dots,-1).
$$

**Proof.** A unitary frame exists by the Gram–Schmidt process applied to $h$; in such a frame $h(x,y) = \delta_{ij}x_i\bar y_j$ and the condition $h(Ax,Ay)=h(x,y)$ is $A^{\dagger}A = I$. The determinant has modulus one because $\det(A^{\dagger}A)=|\det A|^2 = 1$, and $SU(m)$ is the kernel of the determinant on $U(m)$; the normal frame of a form of signature $(p,q)$ gives the displayed group. The Gram–Schmidt process and the diagonalisation are *Quadratic Forms and Polarisation* and *Self-Adjoint Operators and the Spectral Theorem*.

**Proposition (the group preserves the frames transitively).** The group $U(h)$ acts transitively on the set of unitary frames of $(V,h)$, and the stabiliser of a frame is the group of unitary diagonal matrices, so the set of unitary frames is $U(m)/T^{m}$ with $T^m$ the compact torus; the group $U(h)$ is a compact Lie group of real dimension $m^2$, and its Lie algebra is the space of skew-adjoint operators, $\mathfrak u(m) = \{X : X^{\dagger} = -X\}$.

**Proof.** Given two unitary frames there is a unique complex-linear map taking one to the other, and it preserves the form because it preserves the $h$-orthonormal coordinates; the stabiliser of a frame consists of the unitaries diagonal in that frame, that is the torus of phases. The compactness is the closedness and boundedness of $U(m)$ in $M_m(\mathbb C)$, the dimension is the real dimension of the skew-Hermitian matrices, $m^2$. This is *Lie Groups* and *The Unitary and Symplectic Groups*.

**Remark (the two actions).** The unitary group acts on $V$ by isometries and on the set of unitary frames transitively but with a stabiliser, and it acts on the space of Hermitian forms of a fixed signature by $h\mapsto h\circ(g\times g)$, on which its orbits are the signatures. The first action is the action on the space of $h$-orthonormal frames, the second the action on the forms; the two are the two natural unitary geometries of the pair $(V,h)$, and they meet in the fact that $U(h)$ is the common stabiliser.

## The Geometries of the Form and of the Frames

**Proposition (the positive-definite forms as a symmetric space).** The set of positive-definite Hermitian forms on $V$ is the homogeneous space $GL(m,\mathbb{C})/U(m)$; it is a symmetric space of noncompact type, and its Riemannian metric is the trace form. The set of Hermitian forms of signature $(p,q)$ is the orbit $GL(m,\mathbb{C})/U(p,q)$, a symmetric space whose complexification is the compact dual.

**Proof.** $GL(m,\mathbb{C})$ acts transitively on the positive-definite forms by $H\mapsto A^{\dagger}HA$, and the stabiliser of the standard form is $U(m)$; the involution $g\mapsto (g^{\dagger})^{-1}$ gives the symmetric structure, whose fixed-point group is $U(m)$. The signature orbit and the duality are the general homogeneous-space statement of *Homogeneous Spaces* and *Hermitian Symmetric Spaces and the Bergman Metric*.

**Proposition (the Grassmannians as unitary symmetric spaces).** The unitary group $U(m)$ acts transitively on the complex $k$-planes of $V$, with stabiliser $U(k)\times U(m-k)$, so the complex Grassmannian is
$$
\mathrm{Gr}_k(\mathbb{C}^m) = U(m)/(U(k)\times U(m-k)) ,
$$
a compact Hermitian symmetric space with a complex structure and a Kähler metric, the compact dual of the bounded symmetric domain of the same type.

**Proof.** A unitary frame whose first $k$ vectors span a given $k$-plane has the remaining vectors in the orthogonal complement, and two such frames differ by $U(k)\times U(m-k)$, which is the stabiliser by the transitivity of the previous section; the complex structure and the Kähler metric come from the invariant complex structure of the quotient, by *Hermitian Symmetric Spaces and the Bergman Metric* and *The Unitary Group and the Hermitian Symmetric Space*.

**Example (the Fubini–Study geometry and the Hopf fibration).** For $k = 1$ the Grassmannian is the projective space $\mathbb{CP}^{m-1} = U(m)/(U(1)\times U(m-1))$, and the quotient $S^{2m-1}/U(1) = \mathbb{CP}^{m-1}$ is the Hopf fibration; the Fubini–Study metric is the invariant Kähler metric of the quotient, and the unitary group acts on it by holomorphic isometries. The projective space is thus the simplest of the unitary geometries and the model in which the Hermitian form, the unitary frames and the symmetric space are the same structure. This is *Hermitian Symmetric Spaces and the Bergman Metric* and *Kähler Manifolds and the Hermitian Form*.

**Remark (the classical groups).** The Hermitian forms and their unitary groups are the complex member of the classical series: the symmetric forms give the orthogonal groups and the alternating forms the symplectic, and the Hermitian forms the unitary, with $U(m)$ arising from the Hermitian form over $\mathbb C$ just as $O(m)$ and $Sp(m)$ arise from the symmetric and alternating forms; the signatures produce the indefinite families $U(p,q)$ as the orthogonal signatures produce $O(p,q)$. The three families and the coincidences of low dimension are *The Unitary and Symplectic Groups* and *Matrix Groups and Classical Groups*.

## Summary

A Hermitian form $h$ on a complex vector space $V$ is sesquilinear and conjugate-symmetric, determined by its real quadratic function through the polarisation $h(x,y) = \frac14\sum_k i^kq(y+i^kx)$, with Gram matrix $H^{\dagger}=H$ and Sylvester normal form $\sum_{i\le p}|z_i|^2 - \sum_{j>p}|z_j|^2$ classified by the signature $(p,q)$; its real and imaginary parts give $h = g - i\omega$ with $g$ symmetric and $\omega$ alternating, and the complex structure is skew-adjoint, $J^{\dagger}=-J$. A unitary frame is a basis with $h(e_i,e_j)=\delta_{ij}$; in it the form is the standard one and the isometry group is the unitary group $U(m) = \{A : A^{\dagger}A=I\}$, with $SU(m)$ the determinant-one subgroup and $U(p,q)$ the group of the indefinite form. The unitary group acts transitively on the unitary frames with stabiliser the torus, is compact of dimension $m^2$ with Lie algebra the skew-adjoint operators, and the set of positive-definite forms is the symmetric space $GL(m,\mathbb{C})/U(m)$; the complex Grassmannian is $U(m)/(U(k)\times U(m-k))$, a compact Hermitian symmetric space whose rank-one case is the projective space and the Hopf fibration. The forms and the type are *Hermitian Geometry and Almost Complex Structures* and *Kähler Manifolds and the Hermitian Form*; the linear conjugation is *The Involution on a Complex Vector Space*; the signatures and real forms are *Complex Manifolds with an Antiholomorphic Involution*; the symmetric spaces are *Hermitian Symmetric Spaces and the Bergman Metric* and *The Unitary Group and the Hermitian Symmetric Space*; the representations are *Unitary Representations of a Lie Group*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h(x,y)=\overline{h(y,x)}$ | a Hermitian form |
| $H$, $H^{\dagger}=H$ | its Gram matrix |
| $(p,q)$, $p+q=m$ | the signature, Sylvester normal form |
| $h=\tfrac14\sum_k i^kq(y+i^kx)$ | the polarisation |
| $U(m)=\{A:A^{\dagger}A=I\}$ | the unitary group |
| $U(p,q)$ | the unitary group of the form of signature $(p,q)$ |
| $GL(m,\mathbb{C})/U(m)$ | the positive-definite forms |
| $U(m)/(U(k)\times U(m-k))$ | the complex Grassmannian |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the Hermitian forms, the unitary group and the symmetric spaces they define.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2012), for the Gram matrix, the inertia, the polarisation and the unitary group.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for sesquilinear and Hermitian forms, the Sylvester normal form and the classical groups.
- Armand Borel, *Linear Algebraic Groups* (Springer, second edition, 1991), for the unitary group, the Grassmannians and the forms of a fixed signature.
