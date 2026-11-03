# __The SVD Decomposition of Endomorphisms of the Biquaternion Algebra__

## Introduction

**The question.** An endomorphism of the biquaternion algebra is a complex-linear map $F:\mathbb{B}\to\mathbb{B}$. The algebra has complex dimension four, so the endomorphisms form a complex vector space of dimension sixteen, and the question of this article is the following. *What is the shortest way to write an arbitrary endomorphism as a sum of pieces of rank one, and what are the pieces?*

**The answer.** Four pieces, never more, and the pieces are the two-sided operators $X\mapsto\tilde QX\tilde P$, one pair of elements per piece. The first family of parameters is orthonormal, the second is orthogonal, the norms of the second decrease from piece to piece, and the number of pieces is the rank of an associated linear map of the algebra into itself, hence at most four — the dimension of the algebra. This is the singular value decomposition of the endomorphism, and it is the exact analogue, for a map of a four-dimensional complex space into itself, of the decomposition $A=U\Sigma V^{*}$ of an array.

**Two families of pieces.** Two different families of objects of rank one appear in this article, and they must not be taken for one another. The first is the family of the *maps* of rank one, of the form $X\mapsto u\langle X,v\rangle$; it depends on the scalar product alone, and its elements are the terms of the SVD of the endomorphism as a map. The second is the family of the *products* of the multiplication, $X\mapsto\tilde QX\tilde P$; it depends on the product, and its elements are the terms of the four-term decomposition that answers the question above. The two families meet, they are not equal, and the difference between them is one of the two or three things in the article that is worth remembering. §*The Rank-One Endomorphisms* is where the second family enters and where the two are separated.

**Why the question is not trivial.** The endomorphisms of $\mathbb{B}$ form a space of dimension sixteen, and the pieces of rank one form a cone of dimension seven inside it. Sixteen is four times four, and the cone is far from being a subspace: the sum of two pieces of rank one is generally not a piece of rank one. The content of the article is that the cone nevertheless spans the whole space in the strongest possible way — four of its elements suffice for every endomorphism — and that the four can be chosen with orthonormal parameters and decreasing weights.

**The method.** The article proceeds in two stages, and the order matters. The first stage is the SVD of a linear map of a four-dimensional complex space with a scalar product into itself: the adjoint, the spectral theorem for the positive semidefinite self-adjoint operators, the singular values, the two orthonormal bases, the rank cases, the identities, the non-uniqueness, and the truncation. Nothing from the multiplication of the algebra enters this stage. The second stage brings in the multiplication: it identifies the rank-one elements of the endomorphism space with the two-sided operators, and it transports the first stage to them.

**What is used and what is not.** The article is self-contained. The algebra, its product, its Hermitian conjugation and its scalar product are fixed in §*The Carrier*, and the spectral theorem that the SVD needs is proved in §*The Spectral Theorem*, not quoted. No matrix representation of the algebra appears, no Peirce frame, no coefficient array, and no result is imported from a later article of the collection. Everything that is proved here is proved here.

**The order of the article.** The carrier and its scalar product come first, then the adjoint of an endomorphism (§*The Carrier*). The spectral theorem for the self-adjoint positive operators follows, with its proof (§*The Spectral Theorem*). The SVD is then stated and proved, and read geometrically (§*The Decomposition*). The weights are examined: the rank cases, the three identities, the non-uniqueness, and the truncation (§*The Weights*). The multiplication enters last: the rank-one endomorphisms are the two-sided operators, and every endomorphism is a sum of at most four of them (§*The Rank-One Endomorphisms*). The summary collects the statements.

**The letters.** $F$ and $G$ are endomorphisms, $F^{*}$ is the adjoint of $F$, $u$, $v$, $\tilde Q$, $\tilde P$, $X$, $Y$ are elements of the algebra, $\sigma_1,\dots,\sigma_4$ are the singular values, $\mathrm{Id}$ is the identity endomorphism, and $\operatorname{Sc}$ is the scalar part. An operator is written with a capital roman letter and no frame; the two-sided operator of a pair carries the letter $\mathcal T$. The calligraphic font marks the elements of the family that the multiplication produces, and it never names a basis.

**Boundaries.** The algebra and its multiplication table are *The Biquaternion Algebra*; the endomorphisms as a space are *The Endomorphisms of the Biquaternion Algebra*; the two-sided operators as a family, with their cone and their composition law, are *Two-Sided Operators on the Biquaternion Algebra*. The present article is independent of the last two: the ambient space is defined in §*The Carrier*, and the family $\mathcal T_{\tilde Q,\tilde P}$ is defined and used in §*The Rank-One Endomorphisms* without any property taken from elsewhere. The two-sided operators appear at the end and not at the beginning, because the SVD is what makes them the atoms of the theory, and not the other way round.

## The Carrier

### The Algebra and its Four Units

**The units.** The algebra $\mathbb{B}$ is the complex algebra with unit $e_t$ and three further generators $e_x,e_y,e_z$ subject to
$$
e_x^2=e_y^2=e_z^2=-e_t,\qquad e_xe_y=e_z,\quad e_ye_z=e_x,\quad e_ze_x=e_y,
$$
the products being read cyclically and the reversed products being the negatives. Every element is a combination $X=X_te_t+X_xe_x+X_ye_y+X_ze_z$ with complex coefficients, and the four units are a complex basis. The algebra has complex dimension four.

**The scalar part.** Every element is the sum of a scalar part and a vector part,
$$
X=\operatorname{Sc}(X)e_t+\operatorname{Vec}(X),\qquad \operatorname{Sc}(X)=X_t ,
$$
and the scalar part is linear. The three vector units squared are $-e_t$, so the scalar part of a square is $\operatorname{Sc}(X^2)=X_t^2-X_x^2-X_y^2-X_z^2$.

**The conjugation.** The **Hermitian conjugation** of an element is
$$
X^{*}=\bar X_t\,e_t-\bar X_x\,e_x-\bar X_y\,e_y-\bar X_z\,e_z ,
$$
the complex conjugate of the coefficients with the sign changed on the vector part. It is conjugate-linear, involutive, $(X^{*})^{*}=X$, and it reverses the product, $(XY)^{*}=Y^{*}X^{*}$.

**The natural conjugation.** The **natural conjugation** is the same formula without the complex bars,
$$
X^{\natural}=X_t\,e_t-X_x\,e_x-X_y\,e_y-X_z\,e_z ,
$$
and it is complex-linear, involutive, and an involution of the algebra: $(XY)^{\natural}=Y^{\natural}X^{\natural}$. The two conjugations differ by the coefficient conjugation, and the difference is used once, in §*The Rank-One Endomorphisms*.

**The scalar part of a product.** Expanding $XY$ and keeping the unit term,
$$
\operatorname{Sc}(XY)=X_tY_t-X_xY_x-X_yY_y-X_zY_z .
$$
This is a complex bilinear form on pairs of elements, nondegenerate, and it is the only product of the algebra that the spectral theorem will need.

### The Scalar Product

**The form.** The algebra carries the **scalar product**
$$
\langle X,Y\rangle=\operatorname{Sc}(XY^{*})=\sum_{\mu}X_\mu\overline{Y_\mu},
$$
the sum running over the four coefficients. It is linear in the first argument, conjugate-linear in the second, and it is positive definite:
$$
\langle X,X\rangle=|X_t|^2+|X_x|^2+|X_y|^2+|X_z|^2 ,
$$
which is zero only for $X=0$. The **norm** of an element is $\|X\|^2=\langle X,X\rangle$. The algebra is therefore a complex Hilbert space of dimension four, and the space is that of four complex coordinates with the standard form.

**The units are orthonormal.** For two units,
$$
\langle e_\mu,e_\nu\rangle=\delta_{\mu\nu},
$$
because $e_\mu e_\nu^{*}$ has scalar part one at $\mu=\nu$ and no scalar part otherwise. The four units are an orthonormal basis, so they are the best possible basis for the decomposition, and every expansion below uses them without loss.

**The expansion.** In an orthonormal basis each element is the sum of its projections,
$$
X=\sum_{\mu}\langle X,e_\mu\rangle e_\mu ,
\qquad
\|X\|^2=\sum_\mu|\langle X,e_\mu\rangle|^2 .
$$
This is the only place where the basis is used, and it is used only to say that the sum of the four projections is the identity.

**The conjugate-linear identification.** Every linear functional on the algebra is $X\mapsto\langle X,\eta\rangle$ for one element $\eta$, and the element is unique. This is the Riesz representation, and it is used twice: once for the adjoint, once for the contraction that produces the two-sided decomposition.

### The Endomorphisms and their Adjoints

**The space.** An **endomorphism** is a complex-linear map $F:\mathbb{B}\to\mathbb{B}$. The endomorphisms form a complex algebra $\operatorname{End}(\mathbb{B})$ under composition, of complex dimension $16$, with the identity $\mathrm{Id}$.

**The two norms.** The **operator norm** and the **mean square norm** of an endomorphism are
$$
\|F\|_{\mathrm{op}}=\sup_{\|X\|=1}\|F(X)\| ,
\qquad
\|F\|^2=\sum_{\mu}\|F(e_\mu)\|^2 ,
$$
$$
The second is the Hilbert–Schmidt norm: the sum of the squares of the images of the four units, computed from any orthonormal basis with the same value. It is the norm used everywhere below, and with it $\|\mathrm{Id}\|^2=4$ and, as will follow from the SVD, $\|F\|^2=\sigma_1^2+\sigma_2^2+\sigma_3^2+\sigma_4^2$.

**The scalar product of operators.** The corresponding scalar product on the endomorphisms is
$$
\langle\!\langle F,G\rangle\!\rangle=\sum_{\mu}\langle F(e_\mu),G(e_\mu)\rangle ,
$$
which is Hermitian and positive definite, and which makes $\operatorname{End}(\mathbb{B})$ a Hilbert space of dimension sixteen.

**The determinant.** The endomorphism $F$ acts on the top exterior power $\Lambda^{4}\mathbb{B}$, which is a complex line, by multiplication by a scalar. That scalar is the **determinant** $\det F$. It is basis-free, it is multiplicative, $\det(FG)=\det F\det G$, and $\det F\neq0$ exactly when $F$ is invertible.

**The adjoint.** Let $F$ be an endomorphism. For each $Y$ the assignment $X\mapsto\langle F(X),Y\rangle$ is a linear functional of $X$, so by the Riesz representation there is exactly one element $F^{*}(Y)$ with
$$
\langle F(X),Y\rangle=\langle X,F^{*}(Y)\rangle
\qquad\text{for all }X .
$$
The assignment $Y\mapsto F^{*}(Y)$ is linear, and it defines the **adjoint** $F^{*}$ of $F$. The adjoint is characterised by the display, and it is unique.

**The rules.** From the characterisation,
$$
(F+G)^{*}=F^{*}+G^{*},\qquad (\lambda F)^{*}=\bar\lambda F^{*},\qquad (FG)^{*}=G^{*}F^{*},\qquad (F^{*})^{*}=F ,
$$
the reversal in the third being the reversal of the product in the algebra read through the form. The adjoint of the identity is the identity, and the adjoint of an invertible endomorphism is the adjoint of its inverse.

**Self-adjoint and positive.** An endomorphism is **self-adjoint** when $F^{*}=F$. It is **positive semidefinite** when it is self-adjoint and
$$
\langle F(X),X\rangle\ge0\qquad\text{for every }X .
$$
For a self-adjoint $F$ the number $\langle F(X),X\rangle$ is real for every $X$, so the inequality is meaningful. The product $F^{*}F$ is the model case:
$$
\langle F^{*}F(X),X\rangle=\langle F(X),F(X)\rangle=\|F(X)\|^2\ge0 ,
$$
and $F^{*}F$ is self-adjoint because $(F^{*}F)^{*}=F^{*}F$. Moreover $F^{*}F=0$ exactly when $F=0$, since $\langle F^{*}F(X),X\rangle=\|F(X)\|^2$.

## The Spectral Theorem

### The Statement

**Theorem (the spectral theorem for positive semidefinite operators).** Let $H$ be a self-adjoint positive semidefinite endomorphism of $\mathbb{B}$. Then the algebra has an orthonormal basis $v_1,v_2,v_3,v_4$ of eigenvectors of $H$,
$$
H(v_i)=\lambda_i v_i,\qquad \lambda_i\ge0 ,
$$
and the eigenvalues can be ordered $\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\ge0$.

The theorem is the whole engine of the article: the SVD is this theorem applied to $F^{*}F$. It is proved here, in four steps, and the proof uses nothing but the compactness of the unit sphere in a finite-dimensional complex space and the definition of the adjoint.

### The Proof

**First step: the maximum exists.** The unit sphere $S=\{X:\|X\|=1\}$ is closed and bounded in $\mathbb{C}^4$, hence compact, and the function $X\mapsto\langle H(X),X\rangle$ is continuous and real-valued on it. So it attains a maximum, $\lambda$, and $\lambda\ge0$ because the operator is positive semidefinite and $S$ is non-empty. Fix a point $v$ of the sphere at which the maximum is attained.

**Second step: the maximising point is an eigenvector.** Let $Y$ be any element and let $t$ be real and small. Put
$$
\boldsymbol{x}(t)=\frac{v+tY}{\|v+tY\|} .
$$
The point $\boldsymbol{x}(t)$ lies on the sphere, so the function
$$
\varphi(t)=\frac{\langle H(v+tY),v+tY\rangle}{\|v+tY\|^{2}}
$$
has a maximum at $t=0$, and therefore $\varphi'(0)=0$. The numerator is $\lambda+2t\operatorname{Re}\langle H(v),Y\rangle+t^2\langle H(Y),Y\rangle$ and the denominator is $1+2t\operatorname{Re}\langle v,Y\rangle+t^2\|Y\|^2$, both because $\|v\|=1$ and $\langle H(v),v\rangle=\lambda$. Differentiating the quotient at $t=0$ and using $\varphi'(0)=0$,
$$
\operatorname{Re}\bigl\langle H(v)-\lambda v,\ Y\bigr\rangle=0 .
$$
The relation holds for every $Y$. Replacing $Y$ by $iY$ turns the real part of $i$ times a number into minus the imaginary part, so the imaginary part vanishes as well, and
$$
H(v)=\lambda v .
$$
The maximising point is an eigenvector, with the real eigenvalue $\lambda\ge0$.

**Third step: the orthogonal complement is invariant.** Let $v^{\perp}$ be the set of elements orthogonal to $v$. If $X$ lies in $v^{\perp}$ then
$$
\langle H(X),v\rangle=\langle X,H(v)\rangle=\lambda\langle X,v\rangle=0 ,
$$
so $H(X)$ lies in $v^{\perp}$ as well. The complement is therefore carried into itself by $H$, and its dimension is three.

**Fourth step: induction.** The restriction of $H$ to $v^{\perp}$ is self-adjoint and positive semidefinite for the restricted form: self-adjoint because $H$ preserves the complement and is self-adjoint on the whole space, positive because the inequality holds on a subspace. The first three steps therefore apply again, and produce a unit eigenvector $v_2$ in $v^{\perp}$ with eigenvalue $\lambda_2\ge0$, then a third in the complement of the first two, then a fourth. After four steps the four eigenvectors are orthonormal and they span, since four orthonormal elements in a space of dimension four are a basis. Ordering the eigenvalues decreasingly gives the statement. $\square$

**Remark on the two conventions.** The proof uses only two facts: the form is positive definite, and the adjoint exists with the defining relation. Both hold for any finite-dimensional complex space with a scalar product, so the theorem is the standard one; it is proved here because the article uses it and does not import it.

### What Follows

**The eigenvalues are the diagonal values.** In the orthonormal eigenbasis the operator is diagonal, so
$$
H=\sum_{i}\lambda_i\,v_i\langle\cdot,v_i\rangle ,
\qquad
\|H\|^2=\sum_i\lambda_i^2 ,
$$
the second because the mean square of a diagonal operator is the mean square of its diagonal.

**The square root.** A positive semidefinite operator has a positive semidefinite square root, and in the eigenbasis it is the operator with the same eigenvectors and the eigenvalues $\sqrt{\lambda_i}$. It is unique, it commutes with $H$, and its square is $H$.

**The kernel.** The kernel of a positive semidefinite operator is spanned by the eigenvectors of eigenvalue zero, because $\langle H(X),X\rangle=0$ forces $H(X)=0$ for such an operator, and $\langle H(X),X\rangle=\sum_i\lambda_i|\langle X,v_i\rangle|^2$.

## The Decomposition

### The Theorem

**Theorem (the singular value decomposition).** Let $F$ be an endomorphism of $\mathbb{B}$. There are orthonormal families $u_1,\dots,u_4$ and $v_1,\dots,v_4$ of the algebra, and real numbers
$$
\sigma_1\ge\sigma_2\ge\sigma_3\ge\sigma_4\ge0 ,
$$
such that
$$
F(v_i)=\sigma_i\,u_i\qquad\text{for }i=1,2,3,4 ,
$$
and equivalently
$$
F=\sum_{i=1}^{4}\sigma_i\,u_i\langle\cdot,v_i\rangle ,
\qquad\text{that is}\qquad
F(X)=\sum_{i=1}^{4}\sigma_i\,u_i\,\langle X,v_i\rangle\quad\text{for every }X .
$$
The numbers $\sigma_i$ are the **singular values** of $F$, the $u_i$ are its **left singular vectors** and the $v_i$ its **right singular vectors**.

**Proof.** The operator $F^{*}F$ is self-adjoint and positive semidefinite, so by the spectral theorem it has an orthonormal eigenbasis $v_1,\dots,v_4$ with real eigenvalues $\lambda_i\ge0$. Relabel so that $\lambda_1\ge\cdots\ge\lambda_4$. Define
$$
\sigma_i=\sqrt{\lambda_i}\ \ge0 .
$$
For each $i$,
$$
\|F(v_i)\|^2=\langle F(v_i),F(v_i)\rangle=\langle F^{*}F(v_i),v_i\rangle=\lambda_i\langle v_i,v_i\rangle=\sigma_i^2 ,
$$
and $\langle F(v_i),F(v_j)\rangle=\lambda_i\langle v_i,v_j\rangle=0$ for $i\neq j$. For the indices with $\sigma_i>0$ put $u_i=F(v_i)/\sigma_i$; these are orthonormal, because $\langle u_i,u_j\rangle=\langle F(v_i),F(v_j)\rangle/(\sigma_i\sigma_j)=\delta_{ij}$. They are at most four in number, so they can be completed to an orthonormal basis $u_1,\dots,u_4$ by adding arbitrary orthonormal elements to the set, which is possible because an orthonormal family in a space of dimension four is never longer than four and always extends. Then $F(v_i)=\sigma_iu_i$ holds for every $i$: for $\sigma_i>0$ by construction, and for $\sigma_i=0$ because then $F(v_i)=0$ and $\sigma_iu_i=0$.

It remains to identify $F$ on an arbitrary element. Since the $v_i$ are an orthonormal basis, $X=\sum_i\langle X,v_i\rangle v_i$, and by linearity
$$
F(X)=\sum_i\langle X,v_i\rangle F(v_i)=\sum_i\sigma_i\langle X,v_i\rangle u_i .
$$
The display is the statement, with the notation $u\langle\cdot,v\rangle$ for the map $X\mapsto u\langle X,v\rangle$. $\square$

**The compact form.** The terms with $\sigma_i=0$ contribute nothing, so in practice the sum runs over the indices with positive weight. Writing $r$ for the number of these indices,
$$
F=\sum_{i=1}^{r}\sigma_i\,u_i\langle\cdot,v_i\rangle ,
\qquad
\sigma_1\ge\cdots\ge\sigma_r>0 ,
$$
and the convention $\sigma_i=0$ beyond $r$ keeps the four-index form without loss. The number $r$ is computed in §*The Weights*.

### The Two Bases

**The diagonal form.** The two families are orthonormal bases of the same space, and in them the operator is diagonal: it carries the $i$-th vector of the second basis to $\sigma_i$ times the $i$-th vector of the first, and it carries the vectors beyond the $r$-th to zero. Read in these two bases, the endomorphism is the diagonal array of the four weights. This is the whole content of the theorem, and the rest of the article is the reading of its consequences.

**The geometric reading.** The image of the unit sphere of $\mathbb{B}$ is the set of the sums $\sum_i\sigma_i\langle X,v_i\rangle u_i$ with $\|X\|=1$, which is the ellipsoid whose semi-axes are the segments of length $\sigma_i$ along the four directions $u_i$. The singular values are the lengths of those semi-axes, the left singular vectors are their directions, and the right singular vectors are the directions of the sphere that are carried to them. The map is thus a rotation, a scaling of the four coordinates, and a second rotation, in that order — the geometric content of the array identity $A=U\Sigma V^{*}$.

**The extremal reading.** The largest weight is the operator norm,
$$
\sigma_1=\sup_{\|X\|=1}\|F(X)\|=\|F\|_{\mathrm{op}} ,
$$
because $\|F(X)\|^2=\sum_i\sigma_i^2|\langle X,v_i\rangle|^2\le\sigma_1^2\|X\|^2$ with equality at $X=v_1$. The smallest weight of the four, allowing zeros, measures how far $F$ is from being invertible.

**The kernel and the image.** From $F(X)=\sum_i\sigma_i\langle X,v_i\rangle u_i$,
$$
\ker F=\operatorname{span}\{v_i:\sigma_i=0\},
\qquad
\operatorname{im}F=\operatorname{span}\{u_i:\sigma_i>0\} .
$$
The first is the set of directions the map crushes, the second the set of directions it reaches. The two are orthogonal families, of dimensions $4-r$ and $r$, and the sum of the two dimensions is four — which is the rank–nullity theorem for this space, read off the decomposition.

### What the Decomposition Means

**The pieces.** Write an **elementary endomorphism** — the phrase is used here in the sense of the SVD and nowhere else — for a map of the form
$$
\mathcal P_{u,v}(X)=u\,\langle X,v\rangle ,\qquad u\neq0,\ v\neq0 .
$$
Then $F=\sum_{i\le r}\sigma_i\mathcal P_{u_i,v_i}$ is a sum of $r$ elementary endomorphisms with non-negative weights, and this is the form in which the SVD answers the question of the introduction: *how many pieces of rank one,* and *which*.

**The rank.** The image of $\mathcal P_{u,v}$ is the line $\mathbb{C}u$, so an elementary endomorphism has image of dimension one; and conversely every endomorphism with image of dimension one is $\mathcal P_{u,v}$ for the generator $u$ of its image and the element $v$ that represents the functional $X\mapsto$ the coordinate of $F(X)$ along $u$. The elementary endomorphisms are therefore exactly the endomorphisms of rank one. This is a statement about the image, and it is not the last word on the subject: §*The Rank-One Endomorphisms* introduces a second family of atoms, defined by the multiplication, and the two families are not the same.

**The normalisation.** The norm of an elementary endomorphism is
$$
\|\mathcal P_{u,v}\|^2=\sum_\mu\|u\langle e_\mu,v\rangle\|^2=\|u\|^2\|v\|^2 ,
$$
because $\sum_\mu|\langle e_\mu,v\rangle|^2=\|v\|^2$. With orthonormal $u$ and $v$ the norm is one, and the weights of the SVD carry the size of the operator: this is the reason the four terms of the decomposition are ordered by weight and not by anything else.

## The Weights

### The Rank Cases

**The number of nonzero weights is the rank.** Let $r$ be the number of indices with $\sigma_i>0$. The image is spanned by the $r$ orthonormal elements $u_1,\dots,u_r$, so $\dim\operatorname{im}F=r$; and conversely if the image has dimension $r$ then exactly $r$ of the weights are positive, by the description of the image above. Hence
$$
r=\operatorname{rk}F ,
$$
and the decomposition has exactly $\operatorname{rk}F$ terms.

**The five cases.** Since the space has dimension four, the possibilities are:

| $\operatorname{rk}F$ | the weights | the decomposition |
|---|---|---|
| $4$ | $\sigma_1\ge\sigma_2\ge\sigma_3\ge\sigma_4>0$ | four terms, $F$ invertible |
| $3$ | $\sigma_4=0$ | three terms, image of dimension three |
| $2$ | $\sigma_3=\sigma_4=0$ | two terms, image of dimension two |
| $1$ | $\sigma_2=\sigma_3=\sigma_4=0$ | one term, $F=\sigma_1u_1\langle\cdot,v_1\rangle$ |
| $0$ | all zero | $F=0$ |

The rank is therefore not an extra invariant: it is the number of terms, and the number of terms is the number of nonzero weights. Inverting the table, an endomorphism is a single elementary endomorphism exactly when its rank is one, and it is a sum of at most three exactly when the fourth weight vanishes.

**The generic case.** For a generic endomorphism the four weights are distinct and positive, and the decomposition has four terms. Degeneracies of the weights are the vanishing of one equation each, so they form a set of measure zero; the case $r=4$ is the open dense case, and it is the case in which the four-term bound is attained.

### The Three Identities

**The product is the determinant.** Multiplying the four weights,
$$
\sigma_1\sigma_2\sigma_3\sigma_4=\bigl|\det F\bigr| .
$$
The reason is the determinantal identity $\det(F^{*}F)=|\det F|^2$ and the spectral theorem applied to $F^{*}F$, whose determinant is the product of its eigenvalues $\lambda_i=\sigma_i^2$; taking square roots gives the display.

**The sum of squares is the norm.** Summing the squares,
$$
\sigma_1^2+\sigma_2^2+\sigma_3^2+\sigma_4^2=\|F\|^2=\sum_\mu\|F(e_\mu)\|^2 .
$$
This is the Pythagorean theorem for the decomposition: the terms are orthogonal in the operator scalar product, because $\langle\!\langle u_i\langle\cdot,v_i\rangle,u_j\langle\cdot,v_j\rangle\rangle$ vanishes for $i\neq j$ when both families are orthonormal. The weight vector therefore carries the whole size of the operator, and a truncation that discards small weights loses exactly their squares.

**The largest weight is the norm.** The first weight is $\|F\|_{\mathrm{op}}$ and the last weight, when the rank is four, is $1/\|F^{-1}\|_{\mathrm{op}}$, the reciprocal of the norm of the inverse. The four weights are thus the natural measure of the operator: they bound its action from above, its inverse from below, and its volume change exactly.

### The Non-Uniqueness

**Where the freedom is.** The weights are determined by $F$ up to order: they are the square roots of the eigenvalues of $F^{*}F$, and eigenvalues are intrinsic. The two families are not. The freedom has three regimes.

**Distinct positive weights.** If the four weights are distinct and positive, the right singular vectors are the eigenvectors of $F^{*}F$ for distinct eigenvalues, hence determined up to a phase each, and the left vectors follow from $u_i=F(v_i)/\sigma_i$. The decomposition is unique up to the simultaneous change
$$
u_i\mapsto e^{i\theta_i}u_i ,\qquad v_i\mapsto e^{i\theta_i}v_i ,
$$
one arbitrary phase per term, and the phases do not mix the terms.

**Coincident weights.** If some weights coincide, the eigenvectors of $F^{*}F$ for a common eigenvalue span a subspace of that dimension, and any orthonormal basis of that subspace is admissible; the corresponding left vectors move with it by the same rotation. The freedom is then a unitary mixing inside each group of equal weights, and it respects the groups: weights of different value are never mixed.

**Vanishing weights.** If some weights vanish, the corresponding right singular vectors span the kernel, and the corresponding left vectors are unconstrained by $F$: any orthonormal family completing the set of the nonzero left vectors is admissible, and it is chosen by a convention and not by the operator. This is the freedom that the compact form of the decomposition removes, since it drops the vanishing terms altogether.

**The invariant summary.** What the SVD determines intrinsically is the multiset of the four weights, the filtration of the space by the subspaces spanned by the right vectors of the largest weights, and the corresponding lines and subspaces on the left. Everything else in the two families is the choice of a basis inside a subspace.

### The Truncation

**The nearest operator of smaller rank.** Let $s$ be an integer between $0$ and $4$, and let
$$
F_s=\sum_{i\le s}\sigma_i\,u_i\langle\cdot,v_i\rangle
$$
be the sum of the $s$ heaviest terms, of rank at most $s$. Then
$$
\|F-F_s\|^2=\sigma_{s+1}^2+\cdots+\sigma_4^2 ,
$$
because the difference is the sum of the discarded terms and those terms are orthogonal to the kept ones. Moreover no endomorphism of rank at most $s$ is closer:
$$
\|F-G\|\ \ge\ \Bigl(\sigma_{s+1}^2+\cdots+\sigma_4^2\Bigr)^{1/2}
\qquad\text{for every }G\text{ with }\operatorname{rk}G\le s .
$$
This is the Eckart–Young theorem. Its content is that the best approximation by a map of smaller rank is obtained by keeping the largest weights and discarding the rest, and that the error is measured by exactly the discarded weight. The rest of the subsection proves it.

**The min-max characterisation.** The proof of the optimality rests on one lemma, and the lemma is a consequence of the decomposition. For $k=1,\dots,4$,
$$
\sigma_k=\min_{\dim W=5-k}\ \max_{0\neq X\in W}\frac{\|F(X)\|}{\|X\|} .
$$
*Proof.* Take $W=\operatorname{span}\{v_k,v_{k+1},v_{k+2},v_{k+3}\}$, of dimension $5-k$. On it the ratio is at most $\sigma_k$, because $\|F(X)\|^2=\sum_{i\ge k}\sigma_i^2|\langle X,v_i\rangle|^2\le\sigma_k^2\|X\|^2$. Conversely let $W$ be any subspace of dimension $5-k$. It meets $\operatorname{span}\{v_1,\dots,v_k\}$ in a non-zero element $X$, since the two dimensions sum to $5$ and the space has dimension four, and there the ratio is at least $\sigma_k$, because $\|F(X)\|^2=\sum_{i\le k}\sigma_i^2|\langle X,v_i\rangle|^2\ge\sigma_k^2\|X\|^2$. The minimum over $W$ is therefore $\sigma_k$. $\square$

**The interlacing.** The lemma gives $\sigma_k(F)\le\sigma_{k-s}(F-G)$ whenever $G$ has rank at most $s$, and the argument is three lines. Let $W$ be a subspace of dimension $5-k+s$ on which $F-G$ is bounded by $\sigma_{k-s}(F-G)$, which exists by the lemma applied to $F-G$. The kernel of $G$ has dimension at least $4-s$, so $W\cap\ker G$ has dimension at least $(5-k+s)+(4-s)-4=5-k$. On that intersection $G$ vanishes, so
$$
\|F(X)\|=\|(F-G)(X)\|\ \le\ \sigma_{k-s}(F-G)\,\|X\| ,
$$
and the min-max formula for $\sigma_k(F)$ — a minimum over subspaces of dimension $5-k$, of which $W\cap\ker G$ is one — gives the inequality.

**The conclusion.** Summing the squares of the interlacing over $k>s$,
$$
\|F-G\|^{2}=\sum_{k}\sigma_k(F-G)^2\ \ge\ \sum_{k>s}\sigma_k(F)^2 ,
$$
for every $G$ of rank at most $s$, with equality for the truncation $F_s$. The nearest endomorphism of rank at most $s$ is therefore the sum of the $s$ heaviest terms, and the error is the square root of the sum of the squares of the discarded weights.

**The reading.** The SVD answers two questions at once: how many rank-one terms are needed to write the operator exactly, and which of them to keep to write it approximately. The answer to the first is the number of nonzero weights, the answer to the second is the largest ones, and the same four numbers serve both.

## The Rank-One Endomorphisms

### The Atoms of the Multiplication

**A second family of atoms.** The elementary endomorphisms $\mathcal P_{u,v}$ depend on the scalar product alone. The algebra has a product, and the product produces its own rank-one objects: for two elements $\tilde Q,\tilde P$,
$$
\mathcal T_{\tilde Q,\tilde P}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
\mathcal T_{\tilde Q,\tilde P}(X)=\tilde Q\,X\,\tilde P ,
$$
the **two-sided operator** of the pair. The pair are the two multipliers, on the left and on the right, and $X$ is the argument. At $\tilde P=e_t$ the operator is the left multiplier $X\mapsto\tilde QX$, at $\tilde Q=e_t$ it is the right multiplier $X\mapsto X\tilde P$, and at the pair $(e_t,e_t)$ it is the identity.

**The composition.** For two pairs,
$$
\mathcal T_{\tilde Q,\tilde P}\,\mathcal T_{\tilde R,\tilde S}=\mathcal T_{\tilde Q\tilde R,\ \tilde S\tilde P} ,
$$
the second slot reversed, because the product is associative and the right multiplier runs backwards. The family is closed under composition, and the reversal is the trace of the anti-representation carried by the right multipliers.

**The cone.** The family is the image of a bilinear map of the pair $(\tilde Q,\tilde P)$, so it is closed under multiplication by a scalar and not under addition: it is a cone, of complex dimension $7$ — eight parameters less the one-dimensional scaling $(\tilde Q,\tilde P)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde P)$ that leaves the operator fixed — inside the sixteen-dimensional space of the endomorphisms. Its elements are the **rank-one endomorphisms** in the sense of the multiplication, and the point of the section is that they, and not the $\mathcal P_{u,v}$, are the atoms of the four-term decomposition.

**Two senses of one word.** The two families are different, and the difference is worth one paragraph. The operator $\mathcal P_{u,v}$ has an image of dimension one: it is rank one as a map. The operator $\mathcal T_{\tilde Q,\tilde P}$ has the image $\tilde Q\mathbb{B}\tilde P$, whose dimension is $\operatorname{rk}(\tilde Q)\operatorname{rk}(\tilde P)$ in the sense of the multipliers, so it is rank one as a map only when both parameters are degenerate. It is nevertheless rank one in the sense that counts here: it is one product, one point of the cone, the smallest object of the additive theory. The decomposition of §*The Decomposition* counts maps of rank one; the decomposition of the next subsection counts products, and the two counts answer different questions.

### The Four-Term Theorem

**The theorem.** Every endomorphism of $\mathbb{B}$ is a sum of at most four two-sided operators, and four is attained. More precisely, for every $F$ there are elements $\tilde Q_1,\dots,\tilde Q_r$ and $\tilde P_1,\dots,\tilde P_r$ of the algebra, with $r\le4$, such that
$$
F=\sum_{i\le r}\mathcal T_{\tilde Q_i,\tilde P_i},
$$
and the smallest such $r$ is a property of $F$ alone.

**The tensor square.** The proof needs the family of the products of pairs, and the natural object is the tensor square $\mathbb{B}\otimes\mathbb{B}$, spanned by the pure tensors $\tilde Q\otimes\tilde P$, of complex dimension sixteen. The bilinear map
$$
\Phi:\mathbb{B}\otimes\mathbb{B}\longrightarrow\operatorname{End}(\mathbb{B}),
\qquad
\Phi(\tilde Q\otimes\tilde P)=\mathcal T_{\tilde Q,\tilde P} ,
$$
is linear on the tensor square and it sends the sixteen pure tensors of the units to the sixteen operators $\mathcal T_{e_\mu,e_\nu}$. Those sixteen are orthonormal for the operator scalar product:
$$
\bigl\langle\!\bigl\langle\mathcal T_{e_\mu,e_\nu},\mathcal T_{e_\rho,e_\sigma}\bigr\rangle\!\bigr\rangle=4\,\delta_{\mu\rho}\,\delta_{\nu\sigma},
$$
because each of the four elements $e_\mu e_\alpha e_\nu$ is a unit up to a sign, the four of them are distinct, and they meet the four elements $e_\rho e_\alpha e_\sigma$ in the same place for the same $\alpha$ only when the two pairs agree. Sixteen mutually orthogonal elements of norm two in a space of dimension sixteen are a basis, so $\Phi$ is an isomorphism of inner-product spaces, and it doubles lengths:
$$
\bigl\|\mathcal T_{\tilde Q,\tilde P}\bigr\|=2\,\|\tilde Q\|\,\|\tilde P\| .
$$

**The contraction.** Since $\Phi$ is an isomorphism, each endomorphism $F$ is the image of exactly one tensor, and the **contraction** of that tensor is the linear map
$$
\varphi_F:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
\bigl\langle\varphi_F(Y),X\bigr\rangle=\bigl\langle\!\bigl\langle\Phi^{-1}(F),\ X\otimes Y\bigr\rangle\!\bigr\rangle ,
$$
the inner product of the tensor with the pure tensor $X\otimes Y$. For a single product, $\Phi^{-1}(\mathcal T_{\tilde Q,\tilde P})=\tilde Q\otimes\tilde P$ and
$$
\varphi_{\mathcal T_{\tilde Q,\tilde P}}(Y)=\tilde Q\,\langle Y,\tilde P\rangle ,
$$
so the contraction of a single product is the elementary endomorphism of the pair, with the product of the algebra in place of the scalar coefficient. For a sum the contraction is the sum of the contractions, by linearity.

**The least number is the rank.** The **length** $\ell(F)$ of an endomorphism is the least number of two-sided operators whose sum is $F$, with $\ell(0)=0$. Then
$$
\ell(F)=\operatorname{rk}\varphi_F\ \le\ \dim_{\mathbb{C}}\mathbb{B}=4 .
$$

*Proof of the first inequality.* If $F=\sum_{i\le r}\mathcal T_{\tilde Q_i,\tilde P_i}$ then $\varphi_F(Y)=\sum_{i\le r}\tilde Q_i\langle Y,\tilde P_i\rangle$, which lies in the span of the $r$ elements $\tilde Q_i$; hence $\operatorname{rk}\varphi_F\le r$, and taking the least $r$ gives $\operatorname{rk}\varphi_F\le\ell(F)$.

*Proof of the second.* Let $\operatorname{rk}\varphi_F=r$ and let $u_1,\dots,u_r$ be a basis of its image. For each $j$ the functional $Y\mapsto\langle\varphi_F(Y),u_j\rangle$ is linear, so it is $\langle Y,\eta_j\rangle$ for one element $\eta_j$, by the Riesz representation; let $\tilde P_j$ be the element representing $\eta_j$ in the other slot. Then
$$
\varphi_F(Y)=\sum_{j\le r}u_j\,\langle Y,\eta_j\rangle ,
$$
because both sides are linear in $Y$ and both take the same values against the basis $u_j$ of the image, and a linear map into the span of a family is determined by its components along that family. The tensor $\sum_j u_j\otimes\tilde P_j$ has the same contractions as $\Phi^{-1}(F)$, since contraction against $X\otimes Y$ gives $\sum_j\langle u_j,X\rangle\langle\tilde P_j,Y\rangle$, and a tensor is determined by its contractions: if a tensor has all of them zero, write it as a sum with independent second factors, choose $Y$ dual to one of them, and the corresponding first factor vanishes. Hence $\Phi^{-1}(F)=\sum_j u_j\otimes\tilde P_j$, that is $F=\sum_{j\le r}\mathcal T_{u_j,\tilde P_j}$, and $\ell(F)\le r$. The two inequalities give the equality, and the bound four is the dimension of the target of $\varphi_F$. $\square$

**The orthonormal form.** The theorem gives the least number of terms; the SVD gives the best choice of them. Apply §*The Decomposition* to the contraction: there are orthonormal families $u_1,\dots,u_r$ and $w_1,\dots,w_r$ and numbers $\varsigma_1\ge\cdots\ge\varsigma_r>0$ with
$$
\varphi_F=\sum_{i\le r}\varsigma_i\,u_i\langle\cdot,w_i\rangle .
$$
The corresponding tensor is $\sum_i\varsigma_i\,u_i\otimes w_i$, so
$$
F=\sum_{i\le r}\varsigma_i\,\mathcal T_{u_i,w_i},
$$
with the $u_i$ orthonormal, the $w_i$ orthonormal, and the numbers positive and ordered. Absorbing the weight into the second parameter,
$$
F=\sum_{i\le r}\mathcal T_{\tilde Q_i,\tilde P_i}
\qquad\text{with the }\tilde Q_i\text{ orthonormal and the }\tilde P_i\text{ mutually orthogonal of norms }\varsigma_i .
$$
The length is the number of terms, and the numbers $\varsigma_i$ are the weights that the contraction produces.

**A caution about the two sets of numbers.** The $\varsigma_i$ are not in general the $\sigma_i$ of §*The Decomposition*, and the reason is structural: the two decompositions of $F$ are two different sums of two different atoms, and they agree in the number of terms only when the rank happens to be the same. The identity shows the extreme case — one product of weight one, and four map-weights equal to one — and the projection of §*The Two Extreme Examples* shows the other — four products, and a single map-weight. What the two decompositions share is the length of the second, the rank of the first: the number $r$, which is four at most in either case.

**The count.** The two numbers of the section are worth setting side by side. Sixteen is the dimension of the space of the endomorphisms, and it is the number of pairs of basis indices, hence the number of terms in the crudest expansion of an operator in the atoms $\mathcal T_{e_\mu,e_\nu}$. Four is the dimension of the algebra, and it is the largest possible length, hence the number of terms in the shortest expansion of an arbitrary operator. The passage from sixteen to four is the passage from the tensor square to one of its factors, and it is the whole content of the theorem.

### The Two Extreme Examples

**The projection onto the scalar line.** Let
$$
\pi:\mathbb{B}\longrightarrow\mathbb{B},\qquad \pi(X)=\operatorname{Sc}(X)\,e_t ,
$$
the projection onto the line of the unit along the vector part. It has rank one, so its SVD has a single term and a single weight; and as a two-sided operator it is a sum of four:
$$
\pi=\tfrac14\bigl(\mathcal T_{e_t,e_t}-\mathcal T_{e_x,e_x}-\mathcal T_{e_y,e_y}-\mathcal T_{e_z,e_z}\bigr).
$$
The four signs are the four values of the scalar part of a square of a unit, $\operatorname{Sc}(e_\mu e_\mu)=1$ for the unit and $-1$ for the three vector units, and the display says that a map of rank one can need the maximal number of products: its image is a line, and the line has to be reached from four directions.

**The natural conjugation.** The natural conjugation is a sum of the same four products with equal signs:
$$
\sum_{\mu}\mathcal T_{e_\mu,e_\mu}=-2\,D ,
\qquad\text{that is}\qquad
\sum_\mu e_\mu\,X\,e_\mu=-2\,X^{\natural}.
$$
The identity is the operator form of the multiplication table: the four sandwiches at the units, added, give the natural conjugation up to the factor $-2$. It confirms the count from the other side, since a sum of four products is the most that can be needed and this one is a single, natural operator.

**The two by two.** The two examples are the four corners of the subject:

| | $\operatorname{rk}F=1$ | $\operatorname{rk}F=4$ |
|---|---|---|
| $\ell(F)=1$ | $\mathcal T_{\tilde\Pi_+,\tilde\Pi_+}$ | $\mathrm{Id}$ |
| $\ell(F)=4$ | the projection $\pi$ | the natural conjugation $D$ |

The table is the reason the two notions must be kept apart. The identity is a single product and has rank four. The projection has rank one and length four. Between them, the elementary endomorphism at a degenerate pair has both numbers equal to one, and the natural conjugation has both equal to four. Nothing relates the two numbers except the bounds $1\le$ each $\le4$.

**The elementary endomorphisms of the multiplication.** The map $\mathcal T_{\tilde Q,\tilde P}$ has an image of dimension $\operatorname{rk}(\tilde Q)\operatorname{rk}(\tilde P)$, the product of the ranks of its two multipliers, each of which is $0$, $1$ or $2$. The four possible values are $0,1,2,4$, and the value three does not occur. A single product is therefore of rank four exactly when both its parameters are invertible, of rank one exactly when both are degenerate, and of rank two in the mixed case. This is the precise sense in which the atoms of the multiplication are not the maps of rank one, and it is the last thing the article needs to say about them.

## Summary

Every endomorphism of the biquaternion algebra is a sum of at most four two-sided operators $\mathcal T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P$, and four is attained. The least number is the **length** $\ell(F)$, it equals the rank of the **contraction** $\varphi_F$ of $F$, and that rank is at most the dimension four of the algebra — against the sixteen products of the crude expansion, which count the dimension of the space of the endomorphisms.

The engine is the **singular value decomposition**. The algebra is a complex Hilbert space of dimension four with the form $\langle X,Y\rangle=\operatorname{Sc}(XY^{*})$; every endomorphism has an adjoint $F^{*}$; the operator $F^{*}F$ is self-adjoint and positive semidefinite, so the spectral theorem gives it an orthonormal eigenbasis with non-negative eigenvalues $\lambda_i$. Then
$$
F=\sum_{i\le r}\sigma_i\,u_i\langle\cdot,v_i\rangle ,
\qquad
\sigma_i=\sqrt{\lambda_i},\quad r=\operatorname{rk}F ,
$$
with both families orthonormal, the weights decreasing, and the terms ordered by weight. The weights satisfy $\sigma_1\sigma_2\sigma_3\sigma_4=|\det F|$, $\sum_i\sigma_i^2=\|F\|^2$ and $\sigma_1=\|F\|_{\mathrm{op}}$; they are intrinsic, the two families are not, and the freedom is a phase per term at distinct weights, a unitary mixing at coincident weights, and an arbitrary completion at vanishing weights. Keeping the largest weights gives the nearest operator of smaller rank, with an error equal to the discarded weights.

Transported through the isometry $\tilde Q\otimes\tilde P\mapsto\mathcal T_{\tilde Q,\tilde P}$, the same decomposition becomes the four-term form of the endomorphism with the two-sided operators as its atoms. The two forms are different decompositions of the same operator, with the same structure and with weights attached to the same rank: the first counts maps of rank one, the second counts products, and the identity — one product, rank four — shows that the two counts cannot be the same count.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sc}(X)$, $X^{\natural}$, $X^{*}$ | the scalar part, the natural conjugation, the Hermitian conjugation |
| $\langle X,Y\rangle$ | the scalar product $\operatorname{Sc}(XY^{*})$, with $\|X\|^2=\langle X,X\rangle$ |
| $F^{*}$ | the adjoint of $F$, $\langle F(X),Y\rangle=\langle X,F^{*}(Y)\rangle$ |
| $\langle\!\langle F,G\rangle\!\rangle$, $\|F\|$ | the operator scalar product and norm, $\sum_\mu\langle Fe_\mu,Ge_\mu\rangle$ |
| $\det F$ | the scalar by which $F$ multiplies the top exterior power |
| $\sigma_i$, $u_i$, $v_i$ | the singular values, the left and the right singular vectors |
| $\mathcal P_{u,v}$ | the elementary endomorphism $X\mapsto u\langle X,v\rangle$ |
| $\mathcal T_{\tilde Q,\tilde P}$ | the two-sided operator $X\mapsto\tilde QX\tilde P$ |
| $\Phi$ | the isometry $\mathbb{B}\otimes\mathbb{B}\to\operatorname{End}(\mathbb{B})$, $\tilde Q\otimes\tilde P\mapsto\mathcal T_{\tilde Q,\tilde P}$ |
| $\varphi_F$, $\ell(F)$ | the contraction of $F$ and its length, the least number of products |
| $\pi$, $D$ | the projection onto $\mathbb{C}e_t$ and the natural conjugation |

## Further Reading

- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the space of the endomorphisms, its dimension and the natural conjugation.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the family $\mathcal T_{\tilde Q,\tilde P}$, its cone and its composition law, treated there in their own right.
- [The Operators on an Algebra](the-operators-on-an-algebra.html), for the ambient operator space in general and the subspace-group rule.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the multiplication table and the two conjugations.
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html) and [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the two slices of the family at the unit.
- [Introduction to the Operator Theory of the Biquaternion Algebra](introduction-to-the-operator-theory-of-the-biquaternion-algebra.html), for the place of the four-term decomposition among the levels of the theory.
