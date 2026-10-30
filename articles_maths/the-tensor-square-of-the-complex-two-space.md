# __The Tensor Square of $\mathbb{C}^2$__

## Introduction

This article treats the tensor square $V\otimes V$ of the complex two-space. The square has complex dimension $4$, and it decomposes canonically into the symmetric square and the alternating square,
$$
V\otimes V=\operatorname{Sym}^2V\oplus\Lambda^2V,\qquad 4=3+1.
$$
The article computes the two summands, identifies the square with the endomorphism algebra once a bilinear form is chosen, defines the twisted product that makes the square an algebra, and reads the decomposition under the classical groups.

The article is the last of the algebraic articles of the category. It does not restate the theory of tensor products, which is *Tensor Products of Algebras* for the universal property and *The Exterior Algebra* for the alternating powers; it does not treat the symmetric algebra in general, which is *The Symmetric Algebra*; and it does not treat the Clifford algebra, which is built on the same square but with a different product. The endomorphism algebra is *The Endomorphisms of $\mathbb{C}^2$*, and the biquaternion reading is *The Biquaternion Algebra*.

**The point of the article is the distinction between what is canonical and what requires a choice.** The decomposition $3+1$ is canonical; the identification of the square with $M_2(\mathbb{C})$ is not, because it needs a nondegenerate bilinear form, and the identification of the two summands with $\mathbb{C}^3$ and $\mathbb{C}$ needs a basis. The twisted product is the algebra structure that the choice of form puts on the square.

## The Tensor Square

**The tensor square has dimension $4$; the swap is an involution with eigenvalues $\pm1$, and its eigenspaces are the symmetric and the alternating squares.**

**Definition.** The **tensor square** is $V\otimes_{\mathbb{C}}V$, the tensor product of the space with itself, with basis $e_i\otimes e_j$ for $i,j\in\{1,2\}$. It is a complex vector space of dimension $4$.

**Definition.** The **swap** is the linear map
$$
\tau:V\otimes V\longrightarrow V\otimes V,\qquad \tau(u\otimes v)=v\otimes u.
$$

**Proposition (the swap is an involution).** The map $\tau$ is well defined, linear, and $\tau^2=\mathrm{id}$; hence $V\otimes V$ is the direct sum of the eigenspaces of $\tau$ for the eigenvalues $+1$ and $-1$.

*Proof.* The map $(u,v)\mapsto v\otimes u$ is bilinear, so it induces a linear map on the tensor product by the universal property. Applying it twice returns $u\otimes v$. An involution with the two eigenvalues $\pm1$ has the eigenspaces $\ker(\tau-\mathrm{id})$ and $\ker(\tau+\mathrm{id})$, whose sum is the whole space because every $x$ is $\tfrac12(x+\tau x)+\tfrac12(x-\tau x)$ and the two summands are independent.

**Definition.** The **symmetric square** is the fixed space
$$
\operatorname{Sym}^2V=\{x:\tau x=x\},
$$
and the **alternating square** is the anti-fixed space
$$
\Lambda^2V=\{x:\tau x=-x\}.
$$

**Theorem (the decomposition).** The tensor square decomposes canonically as
$$
V\otimes V=\operatorname{Sym}^2V\oplus\Lambda^2V,
$$
with dimensions $3$ and $1$ over $\mathbb{C}$, and $6$ and $2$ over $\mathbb{R}$.

*Proof.* The decomposition is the eigenspace decomposition of the involution $\tau$. A basis of the symmetric square is
$$
e_1\otimes e_1,\qquad \tfrac12(e_1\otimes e_2+e_2\otimes e_1),\qquad e_2\otimes e_2,
$$
and a basis of the alternating square is $e_1\wedge e_2=e_1\otimes e_2-e_2\otimes e_1$; the four vectors are independent and four is the dimension.

**Remark (the decomposition is canonical).** No basis, no form and no orientation enter the decomposition: it is the eigenspace decomposition of the swap, which is defined by the tensor product alone. **What is not canonical is the identification of the two summands with $\mathbb{C}^3$ and $\mathbb{C}$**, which needs a basis of $V$ to name the three symmetric vectors and the one alternating vector.

## The Symmetric Square

**The symmetric square has dimension $3$; after a basis it is the space of binary quadratic forms, and the rank-one elements form the Veronese conic in the projective plane.**

**Definition.** The **symmetric product** of two vectors is $u\odot v=\tfrac12(u\otimes v+v\otimes u)$, an element of $\operatorname{Sym}^2V$.

**Proposition (the dimension and the basis).** $\operatorname{Sym}^2V$ has dimension $3$, with basis $e_1\odot e_1$, $e_1\odot e_2$, $e_2\odot e_2$.

*Proof.* The three vectors are fixed by $\tau$ and independent. A fixed tensor $\sum_{ij}c_{ij}e_i\otimes e_j$ satisfies $c_{ij}=c_{ji}$, so it is determined by the three coefficients $c_{11},c_{12},c_{22}$.

**Proposition (binary quadratic forms).** After the choice of the basis, the symmetric square is identified with the space of homogeneous polynomials of degree $2$ in two variables,
$$
\operatorname{Sym}^2V\cong\{aQ_{\blacktriangle}^2+bQ_{\blacktriangle}Q_{\blacktriangledown}+cQ_{\blacktriangledown}^2:a,b,c\in\mathbb{C}\},
$$
of dimension $3$.

*Proof.* The identification sends $e_1\odot e_1$, $e_1\odot e_2=e_2\odot e_1$ and $e_2\odot e_2$ to $Q_{\blacktriangle}^2$, $Q_{\blacktriangle}Q_{\blacktriangledown}$ and $Q_{\blacktriangledown}^2$; the three monomials are a basis, and the correspondence is linear and bijective.

**Definition.** The **Veronese map** is
$$
\nu:\mathbb{P}(V)\longrightarrow\mathbb{P}(\operatorname{Sym}^2V),\qquad[Q]\longmapsto[Q\odot Q].
$$
Its image is the **Veronese conic** in $\mathbb{CP}^2=\mathbb{P}(\operatorname{Sym}^2V)$.

**Proposition (the rank stratification).** An element of $\operatorname{Sym}^2V$ has rank $2$, $1$ or $0$ as a symmetric form. The rank-$1$ elements are exactly the squares $Q\odot Q$ of nonzero vectors, and their projectivisation is the Veronese conic; the rank-$0$ element is $0$.

*Proof.* In a basis, the element is a symmetric bilinear form on $V^{*}$; its rank is the rank of the symmetric matrix. A rank-one symmetric matrix is $QQ^{T}$ for a nonzero vector $Q$, that is $Q\odot Q$; the rank-zero element is the zero matrix. The image of $\nu$ is the set of the classes of the rank-one elements, which is a conic because it is the zero set of the discriminant $b^2-4ac$, an irreducible quadratic.

**Remark (the discriminant and the conic).** The discriminant $\Delta=b^2-4ac$ is the equation of the conic. **The nondegenerate forms are the complement of the conic, the rank-one forms are the conic itself, and the origin is the only rank-zero form**; the conic is smooth because its equation has no repeated factor. The dual conic, read in the dual plane, is the set of the tangent lines, and it is the image of the dual Veronese map.

## The Alternating Square

**The alternating square has dimension $1$; it is the line of the determinant, and the identification of that line with $\mathbb{C}$ needs a basis or a volume form.**

**Definition.** The **alternating product** is $u\wedge v=u\otimes v-v\otimes u$, an element of $\Lambda^2V$.

**Proposition (the dimension and the determinant).** $\Lambda^2V$ has dimension $1$, with basis $e_1\wedge e_2$. For $u=u^1e_1+u^2e_2$ and $v=v^1e_1+v^2e_2$,
$$
u\wedge v=\det\begin{pmatrix}u^1&v^1\\u^2&v^2\end{pmatrix}\,e_1\wedge e_2.
$$

*Proof.* The alternating square is spanned by $e_1\wedge e_2$, and the coefficient of $e_1\wedge e_2$ in $u\wedge v$ is the determinant of the matrix of the two columns $u,v$. The determinant is alternating and bilinear, and it is the only alternating bilinear form on $V$ up to a scalar.

**Proposition (the determinant representation).** For $g\in\mathrm{GL}_2(\mathbb{C})$, the induced map on $\Lambda^2V$ is multiplication by $\det g$; in particular $\mathrm{SL}_2(\mathbb{C})$ acts trivially on $\Lambda^2V$.

*Proof.* The induced map sends $u\wedge v$ to $gu\wedge gv=\det(g)\,u\wedge v$ by the multiplicativity of the determinant.

**Remark (no canonical identification with $\mathbb{C}$).** The line $\Lambda^2V$ is one-dimensional, but **there is no canonical element of it**: the element $e_1\wedge e_2$ depends on the basis, and under a change of basis of determinant $d$ it is multiplied by $d$. A volume form, that is a nonzero element of $\Lambda^2V^{*}$, or a basis of $V$, supplies the identification; the identification is a choice.

## The Isomorphism with the Endomorphism Algebra

**The square is canonically the endomorphism algebra of $V$ only against the dual; identifying it with the endomorphisms of $V$ itself needs a nondegenerate bilinear form.**

**Theorem (the canonical isomorphism).** There is a canonical isomorphism
$$
V\otimes V^{*}\longrightarrow\operatorname{End}(V),\qquad u\otimes\ell\longmapsto\bigl(w\mapsto\ell(w)u\bigr).
$$

*Proof.* The map $(u,\ell)\mapsto(w\mapsto\ell(w)u)$ is bilinear, hence induces a linear map on the tensor product. On the bases, $e_i\otimes\ell^{j}$ is sent to the matrix unit $E_{ij}$: on $e_k$, it gives $\ell^{j}(e_k)e_i=\delta_{jk}e_i$, which is the $k$-th column of $E_{ij}$. The four matrix units are a basis of the endomorphisms, so the map is an isomorphism.

**Theorem (the identification with a form).** Let $F$ be a nondegenerate bilinear form on $V$, and let $F^{\flat}:V\to V^{*}$ be $v\mapsto F(v,\cdot)$. Then the composite
$$
V\otimes V\xrightarrow{\ \mathrm{id}\otimes F^{\flat}\ }V\otimes V^{*}\xrightarrow{\ \cong\ }\operatorname{End}(V)
$$
is an isomorphism, given explicitly by
$$
u\otimes v\longmapsto\bigl(w\mapsto F(v,w)u\bigr).
$$

*Proof.* The form is nondegenerate, so $F^{\flat}$ is an isomorphism; the second map is the canonical isomorphism above. The composite sends $u\otimes v$ to $u\otimes F(v,\cdot)$, that is to the map $w\mapsto F(v,w)u$.

**Corollary (the two summands).** For $F$ symmetric, the isomorphism sends $\operatorname{Sym}^2V$ onto the symmetric endomorphisms with respect to $F$, of dimension $3$, and $\Lambda^2V$ onto the skew endomorphisms, of dimension $1$.

*Proof.* The adjoint of the map $\Phi(u\otimes v):w\mapsto F(v,w)u$ with respect to $F$ is $\Phi(v\otimes u)$, because
$$
F(\Phi(u\otimes v)x,y)=F(v,x)F(u,y)=F(x,\Phi(v\otimes u)y).
$$
Hence the fixed tensors of the swap correspond to the self-adjoint operators and the anti-fixed ones to the skew operators. The dimensions are those of the two eigenspaces.

**Remark (the alternating case).** For $F$ alternating, the adjoint of $\Phi(u\otimes v)$ is $-\Phi(v\otimes u)$; the symmetric tensors correspond to the operators that are skew for $F$, the Lie algebra $\mathfrak{sp}(2)$ of dimension $3$, and the alternating tensors to the scalars. **The decomposition $3+1$ is the same, but its interpretation as symmetric and skew operators depends on the symmetry of the form.**

**Remark (what the choice of form changes).** The isomorphism $V\otimes V\cong\operatorname{End}(V)$ depends on $F$: two forms give two isomorphisms, and their composite is not the identity on the square. **Without a form there is only the canonical isomorphism $V\otimes V^{*}\cong\operatorname{End}(V)$**, which uses the duality and not a metric.

## The Twisted Product

**A nondegenerate bilinear form puts an associative product on the square, with identity the inverse form; the resulting algebra is $M_2(\mathbb{C})$.**

**Definition.** Let $F$ be a nondegenerate bilinear form on $V$. The **twisted product** on $V\otimes V$ is
$$
(u\otimes v)\cdot(u'\otimes v')=F(v,u')\,u\otimes v'.
$$

**Theorem (the algebra structure).** The twisted product is bilinear, associative and unital. Its identity is
$$
1_F=\sum_{i,j}F^{ij}e_i\otimes e_j,
$$
where $F^{ij}$ is the inverse matrix of $F_{ij}=F(e_i,e_j)$. The algebra $(V\otimes V,\cdot_F)$ is isomorphic to $\operatorname{End}(V)$ by the map
$$
\Phi_F(u\otimes v)=\bigl(w\mapsto F(v,w)u\bigr).
$$

*Proof.* Bilinearity is clear. For associativity, both products
$$
\bigl((u\otimes v)(u'\otimes v')\bigr)(u''\otimes v'')=F(v,u')F(v',u'')\,u\otimes v''
$$
and
$$
(u\otimes v)\bigl((u'\otimes v')(u''\otimes v'')\bigr)=F(v,u')F(v',u'')\,u\otimes v''
$$
coincide. For the identity, compute against a basis vector,
$$
1_F\cdot(e_k\otimes v)=\sum_{i,j}F^{ij}F(e_j,e_k)e_i\otimes v=\sum_i\delta^{i}_{k}e_i\otimes v=e_k\otimes v,
$$
and the same on the other side. For the isomorphism, $\Phi_F$ is the composite of the theorem of the previous section, hence bijective, and it is multiplicative:
$$
\Phi_F\bigl((u\otimes v)(u'\otimes v')\bigr)=F(v,u')\Phi_F(u'\otimes v')=\Phi_F(u\otimes v)\Phi_F(u'\otimes v').
$$

**Corollary (the identity is the inverse form).** In the standard basis with $F=I$, the identity is $e_1\otimes e_1+e_2\otimes e_2$; it is the symmetric tensor that corresponds to the identity matrix.

*Proof.* The inverse matrix of the identity is the identity, so $1_F=\sum_i e_i\otimes e_i$.

**Corollary (the two summands are not subalgebras).** The symmetric square is not closed under the twisted product, and neither is the alternating square; the product of two symmetric tensors is symmetric only when the corresponding symmetric matrices commute.

*Proof.* Under $\Phi_F$ with $F$ symmetric, the symmetric square corresponds to the symmetric matrices, and the product of two symmetric matrices is symmetric exactly when they commute: $(AC)^{T}=C^{T}A^{T}=CA$, which equals $AC$ exactly when $AC=CA$. It is not symmetric in general: for
$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad C=\begin{pmatrix}0&1\\1&1\end{pmatrix},
$$
the product $AC=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ is not symmetric. The alternating square corresponds to the skew matrices, and in this dimension the product of two skew matrices is always symmetric, so it also leaves the line.

**Remark (the biquaternion reading).** The algebra $(V\otimes V,\cdot_F)$ is isomorphic to $M_2(\mathbb{C})$, hence to the biquaternion algebra $\mathbb{B}$. **The tensor square with the twisted product is a second copy of the biquaternion algebra, built from the space and a form rather than from the tensor product of the field and the quaternions**; the symmetric and alternating squares are the fixed and anti-fixed spaces of the involution induced by the swap, and they correspond to the symmetric and skew matrices in the model. The algebra is *The Biquaternion Algebra*, and the matrix model is *The Product, the Trace and the Determinant*.

## The Decomposition under the Groups

**Under $\mathrm{SL}_2(\mathbb{C})$ the square is the sum of the spin-one representation of dimension $3$ and the trivial representation; under $\mathrm{GL}_2(\mathbb{C})$ the second summand carries the determinant character.**

**Theorem (the Clebsch–Gordan decomposition).** As representations of $\mathrm{SL}_2(\mathbb{C})$,
$$
V\otimes V\cong\operatorname{Sym}^2V\oplus\Lambda^2V\cong\operatorname{Sym}^2V\oplus\mathbb{C},
$$
where $\operatorname{Sym}^2V$ is irreducible of dimension $3$ and $\Lambda^2V$ is the trivial representation. As representations of $\mathrm{GL}_2(\mathbb{C})$, the second summand is the character $g\mapsto\det g$, and the first is irreducible of dimension $3$.

*Proof.* The group acts on the square by $g(u\otimes v)=gu\otimes gv$ and preserves the swap, hence preserves the two summands. The alternating square is one-dimensional and $g$ acts on it by $\det g$, which is trivial on $\mathrm{SL}_2$. The symmetric square is irreducible: its highest-weight vector is $e_1\odot e_1$, of weight $2$, and the three vectors $e_1\odot e_1$, $e_1\odot e_2$, $e_2\odot e_2$ form a chain under the lowering operator, so no proper subrepresentation exists.

**Remark (the same decomposition in three languages).** The decomposition $2\otimes2=3\oplus1$ is read as the Clebsch–Gordan series of $\mathfrak{sl}_2$, as the decomposition of the tensor square of the spinor of $\mathrm{SU}(2)$ into the vector and the scalar, and as the decomposition of the square of the defining representation of $\mathrm{GL}_2$. **The three readings are the same theorem**, and the dimension count $4=3+1$ is the same count in each.

| Group | $V$ | $\operatorname{Sym}^2V$ | $\Lambda^2V$ |
|---|---|---|---|
| $\mathrm{SL}_2(\mathbb{C})$ | defining, dimension $2$ | irreducible, dimension $3$ | trivial, dimension $1$ |
| $\mathrm{GL}_2(\mathbb{C})$ | defining, dimension $2$ | irreducible, dimension $3$ | the determinant character |
| $\mathrm{U}(2)$ | defining, dimension $2$ | irreducible, dimension $3$ | the determinant character |
| $\mathrm{SU}(2)$ | spinor, dimension $2$ | spin $1$, dimension $3$ | scalar, dimension $1$ |

**Remark (the spin interpretation).** For $\mathrm{SU}(2)$, the space $V$ is the spinor representation of spin $\tfrac12$, the symmetric square is the spin-$1$ representation of dimension $3$, and the alternating square is the scalar of spin $0$. **The tensor square of a spinor is a vector plus a scalar**, which is the elementary case of the addition of angular momenta; the spin representation is *The One-Sided Action and the Spin Representation*, and the groups are *The Classical Groups of $\mathbb{C}^2$*.

## Summary

The tensor square $V\otimes V$ has dimension $4$ and decomposes canonically under the swap into the symmetric square of dimension $3$ and the alternating square of dimension $1$: $4=3+1$, or $6+2$ over $\mathbb{R}$. The symmetric square is, after a basis, the space of binary quadratic forms $aQ_{\blacktriangle}^2+bQ_{\blacktriangle}Q_{\blacktriangledown}+cQ_{\blacktriangledown}^2$, with the rank-one elements forming the Veronese conic $b^2-4ac=0$ in $\mathbb{CP}^2$; the alternating square is the line of the determinant, on which $g$ acts by $\det g$, and it has no canonical generator.

The square is canonically the endomorphism algebra only as $V\otimes V^{*}\cong\operatorname{End}(V)$, by $u\otimes\ell\mapsto(Q\mapsto\ell(Q)u)$. A nondegenerate bilinear form $F$ gives an isomorphism $V\otimes V\cong\operatorname{End}(V)$, $u\otimes v\mapsto(Q\mapsto F(v,Q)u)$, and a twisted product $(u\otimes v)(u'\otimes v')=F(v,u')u\otimes v'$ with identity $\sum_{ij}F^{ij}e_i\otimes e_j$; the resulting algebra is $M_2(\mathbb{C})\cong\mathbb{B}$. For $F$ symmetric the two summands correspond to the symmetric and the skew operators; for $F$ alternating they correspond to $\mathfrak{sp}(2)$ and the scalars. Under $\mathrm{SL}_2(\mathbb{C})$ the square is the sum of the irreducible representation of dimension $3$ and the trivial one, and under $\mathrm{GL}_2(\mathbb{C})$ the second summand is the determinant character.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V\otimes V$ | the tensor square, complex dimension $4$ |
| $\tau(u\otimes v)=v\otimes u$ | the swap, an involution |
| $\operatorname{Sym}^2V$ | the symmetric square, the fixed space of $\tau$, dimension $3$ |
| $\Lambda^2V$ | the alternating square, the anti-fixed space of $\tau$, dimension $1$ |
| $u\odot v=\tfrac12(u\otimes v+v\otimes u)$ | the symmetric product |
| $u\wedge v=u\otimes v-v\otimes u$ | the alternating product |
| $\nu([Q])=[Q\odot Q]$ | the Veronese map, with image the conic $b^2-4ac=0$ |
| $V\otimes V^{*}\cong\operatorname{End}(V)$ | the canonical isomorphism, $u\otimes\ell\mapsto(Q\mapsto\ell(Q)u)$ |
| $F^{\flat}:V\to V^{*}$ | the isomorphism $v\mapsto F(v,\cdot)$ given by a nondegenerate form |
| $(u\otimes v)(u'\otimes v')=F(v,u')u\otimes v'$ | the twisted product |
| $1_F=\sum_{ij}F^{ij}e_i\otimes e_j$ | its identity, the inverse form |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space and its forms.
- [The Endomorphisms of $\mathbb{C}^2$](the-endomorphisms-of-the-complex-two-space.html), the previous article, for the algebra $M_2(\mathbb{C})$ and its identification with the biquaternion algebra.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), for the forms $B$ and $\omega$ used in the twisted product.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ and its simple module.
- [Tensor Products of Algebras](tensor-products-of-algebras.html), for the universal property and the general theory of the tensor product.
- [The Exterior Algebra](the-exterior-algebra.html), for the alternating powers and the determinant.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant as an alternating form.
- [The One-Sided Action and the Spin Representation](the-one-sided-action-and-the-spin-representation.html), for the spin representation and the addition of angular momenta.
