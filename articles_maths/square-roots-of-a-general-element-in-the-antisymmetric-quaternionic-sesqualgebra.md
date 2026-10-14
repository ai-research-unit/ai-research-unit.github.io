# __Square Roots of a General Element in the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

A square root of an element $\tilde R$ in a product $\star$ is an element whose square is $\tilde R$, the equation $\tilde\Xi\star\tilde\Xi=\tilde R$, and the equation is read with the product in force. For the conjugate cross product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\vec P\times\overline{\vec Q}
$$

of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* the equation is decided by one subspace. The value of the square is

$$
\tilde\Xi\diamond\tilde\Xi=\vec\Xi\times\overline{\vec\Xi}=-2i\,\vec a\times\vec b,\qquad \vec\Xi=\vec a+i\vec b,
$$

with $\vec a,\vec b$ real, so the image of the square map is the three real dimensional subspace of the purely imaginary real vectors, and the criterion for the existence of a root is a condition on the element $\tilde R$:

**$\tilde R$ has a square root in the block exactly when its scalar coordinate vanishes and its vector part lies in the three real dimensional subspace spanned by $ie_1,ie_2,ie_3$.**

The criterion is not the vanishing of a quadratic form, as it is in the model block, where the root of an element exists exactly when a certain complex number is a square; it is the membership of a subspace of real dimension three, and it excludes the whole of the real vector subspace and the whole of the central line except the origin. The solution set has a structure of its own: the scalar coordinate of a root is free, and the vector part of the root solves the cross-product equation $\vec a\times\vec b=-\tfrac12\vec w$ for the prescribed $\vec w$, a system of three real equations in two real vectors, whose solution set is of real dimension three in the generic case. The root set is therefore a complex line of roots over a threefold family, of real dimension five, and the examples below show it concretely.

The reading is the continuation of the two companion articles of the block, where the central values are treated as the special case $\tilde R=\lambda e_0$ and the sets are computed: the value $+1$ and the idempotents are *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Sesqualgebra*, and the value $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*; the diagonal of the block, whose image is the subspace above, is *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; the absence of the algebraic norm, which is why the criterion is not a quadratic one, is *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra*; and the model block, where the criterion is the quadratic one, is *Square Roots of a General Element in the General Plain Algebra*.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$, a generic element $\tilde\Xi=\Xi_0e_0+\vec\Xi$ with $\vec\Xi=\sum_k\Xi_ke_k$ and $\Xi_k=x_k+ix'_k$. The three real dimensional subspace of the purely imaginary real vectors is written $i\mathbb{R}^{3}=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$; an element of it is of the form $i\vec w$ with $\vec w$ a real vector. The square map is $\tilde\Xi\mapsto\tilde\Xi\diamond\tilde\Xi$; the part of the geometry of the values that is used below is the identity $\vec a\times(\vec b\times\vec c)=\vec b(\vec a,\vec c)-\vec c(\vec a,\vec b)$ for the complex bilinear dot product of the vector parts.

**The results.** A biquaternion $\tilde R=R_0e_0+\vec R$ has a square root in the block exactly when its scalar coordinate vanishes and its vector part is a purely imaginary real vector, $R_0=0$ and $\vec R=i\vec w$ with $\vec w$ real; the criterion is the membership of the real three-dimensional subspace $i\mathbb{R}^{3}=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, which is the image of the square. The radicands outside it are rootless, among them the whole central line except the origin and the whole real vector subspace except the origin, the real unit $e_3$ included. When the criterion holds with value $i\vec w$, the roots are the elements $\tilde\Xi=\Xi_0e_0+\vec a+i\vec b$ with $\Xi_0\in\mathbb{C}$ free and $\vec a,\vec b$ real solving $\vec a\times\vec b=-\tfrac12\vec w$, so the root set is a complex line over the solution set of that real equation, of real dimension five for a nonzero value and the cone of the diagonal, of real dimension six, for the origin.

## The Definition, Relative to a Product

**Definition (square root of an element).** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde R\in\mathbb{B}$. A **square root of $\tilde R$ in $\star$** is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\tilde R ,
$$

and the **root set** of $\tilde R$ in $\star$ is the set of its square roots. The special case in which $\tilde R=\lambda e_0$ is the root of a central value, which is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*; the definition of the square root of an element and the reading of the root sets for a general element in the model block are *Square Roots of a General Element in the General Plain Algebra*.

Throughout this article the product is the block $\diamond$, so that, unqualified, a root is a square root in the block and the equation is $\tilde\Xi\diamond\tilde\Xi=\vec\Xi\times\overline{\vec\Xi}=\tilde R$. The origin is a root of the origin, and the roots of a general element are read on the vector subspace, since every value of the block is a pure vector.

**Remark (the equation is not linear in the root).** For the block the square is quadratic in the vector part and independent of the scalar coordinate, so the equation is a quadratic system and not a linear one; the scalar coordinate of the root is a free parameter and the vector part solves a system of three quadratic equations in six real unknowns. The reading is therefore a criterion for existence and a description of the root set, and not a formula for the root as a linear function of the element, which is what the model block has for the elements outside its cone.

## The Image of the Square

**For every biquaternion $\tilde\Xi\diamond\tilde\Xi=-2i\,\vec a\times\vec b$ with $\vec\Xi=\vec a+i\vec b$, so the image of the square map is exactly the real three-dimensional subspace $i\mathbb{R}^{3}=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, and it is attained: every real vector $\vec w$ has an element whose square is $i\vec w$.**

**Theorem (the image is the subspace of the purely imaginary real vectors).** For every biquaternion,

$$
\tilde\Xi\diamond\tilde\Xi=-2i\,\vec a\times\vec b,\qquad \vec\Xi=\vec a+i\vec b,
$$

with $\vec a,\vec b$ real; consequently the image of the square map is exactly $i\mathbb{R}^{3}=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, a real subspace of dimension three, and it is attained: for every real vector $\vec w$ there is an element whose square is $i\vec w$.

*Proof.* Write $\vec\Xi=\vec a+i\vec b$ and use the $\mathbb{C}$-bilinearity of the cross product and the conjugate-linearity of the conjugation: $\vec\Xi\times\overline{\vec\Xi}=(\vec a+i\vec b)\times(\vec a-i\vec b)=\vec a\times\vec a-i\,\vec a\times\vec b+i\,\vec b\times\vec a-i^{2}\,\vec b\times\vec b$, and the first term and the last vanish, while $\vec b\times\vec a=-\vec a\times\vec b$, so the two middle terms add: $\vec\Xi\times\overline{\vec\Xi}=-2i\,\vec a\times\vec b$, which lies in $i\mathbb{R}^{3}$ and is real on the imaginary axis, so that the image is contained in $i\mathbb{R}^{3}$. For the converse, let $\vec w$ be a real vector; the value $i\vec w$ with $\vec w=0$ is attained by the origin, and for $\vec w\neq0$ let $\vec u$ be a real vector not parallel to $\vec w$, put $\vec a=\vec w\times\vec u$, so that $\vec a$ is orthogonal to $\vec w$ and nonzero, and put $\vec b=-\tfrac12(\vec w\times\vec a)\lvert\vec a\rvert^{-2}$; then $\vec a\times\vec b=-\tfrac12\vec w$ by the identity $\vec a\times(\vec w\times\vec a)=\vec w\lvert\vec a\rvert^{2}$, since $\vec a$ is orthogonal to $\vec w$, and the element $\tilde\Xi=\vec a+i\vec b$ has square $-2i\,\vec a\times\vec b=i\vec w$.

**Remark (the subspace of the image and the centre).** The image of the square is a real subspace of the vector subspace, and its intersection with the central line is the origin. This is the reason for the emptiness of the roots of the central values other than zero, and it is also the reason for the emptiness of the square roots of the real vector subspace: an element of $\mathbb{R}^{3}$, that is a vector element with real coordinates, is not in $i\mathbb{R}^{3}$ unless it is zero, so no nonzero real direction is a square of the block. The criterion of the next section records both exclusions at once.

## The Criterion

**A biquaternion $\tilde R=R_0e_0+\vec R$ has a square root in the block exactly when $R_0=0$ and $\vec R=i\vec w$ with $\vec w$ real, that is exactly when $\tilde R$ lies in $i\mathbb{R}^{3}$; the roots are then the elements with arbitrary complex scalar coordinate and vector part $\vec a+i\vec b$ solving $\vec a\times\vec b=-\tfrac12\vec w$.**

**Theorem (the criterion for the existence of a root).** Let $\tilde R=R_0e_0+\vec R$ be a biquaternion. Then $\tilde R$ has a square root in the block exactly when

$$
R_0=0 \qquad\text{and}\qquad \vec R=i\vec w\ \text{with}\ \vec w\ \text{real},
$$

that is exactly when $\tilde R$ lies in the subspace $i\mathbb{R}^{3}$ of the purely imaginary real vectors. When the criterion holds and $\tilde R=i\vec w$, the roots of $\tilde R$ are the elements

$$
\tilde\Xi=\Xi_0e_0+\vec a+i\vec b,\qquad \Xi_0\in\mathbb{C},\quad \vec a,\vec b\in\mathbb{R}^{3},\quad \vec a\times\vec b=-\tfrac12\vec w,
$$

with the scalar coordinate free and the two real vectors solving one real cross-product equation.

*Proof.* Necessity: every value of the block is a pure vector, so $R_0=0$, and the image of the square is $i\mathbb{R}^{3}$ by the theorem above, so $\vec R\in i\mathbb{R}^{3}$. Sufficiency: the construction of the same theorem gives one root of $i\vec w$ for every real $\vec w$, and the description of the root set is the reading of the equation in the coordinates of the criterion: the square reads the vector part alone, so the scalar coordinate of the root is free, and the vector part of the root is the real and the imaginary part of $\vec\Xi$, related by $\vec\Xi\times\overline{\vec\Xi}=-2i\,\vec a\times\vec b=i\vec w$.

**Corollary (the excluded elements).** No element of the central line other than the origin has a square root, so the root of a central value exists only for $\lambda=0$; no element of the real vector subspace other than the origin has a square root, so the real directions $e_1,e_2,e_3$ and the real combinations $x_1e_1+x_2e_2+x_3e_3$ are outside the image; and the square roots of the origin are the cone of the diagonal, of real dimension six. The comparison with the three central values is the two companion articles of the block, *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*, where the sets are computed one by one.

**Remark (the criterion is a subspace membership and not a quadratic equation).** In the model block the criterion for the existence of a square root of an element is the solvability of a quadratic equation in the central square of the element, so that the root exists for half of the elements in a precise sense and the root set is discrete outside the cone. For the block the criterion is the membership of a real three dimensional subspace, which is a linear condition on the eight real coordinates of the element, and the root set is not discrete: it is a line over a threefold family. The difference is the difference between a product with an algebraic norm and a product without one, and the block is the second case, as *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra* records.

## The Root Set

**The root set of a value $i\vec w$ is the union, over the solutions $(\vec a,\vec b)$ of $\vec a\times\vec b=-\tfrac12\vec w$, of the complex lines $\Xi_0e_0+\vec a+i\vec b$; it has real dimension five for $\vec w\neq0$, and for $\vec w=0$ it is the cone of the diagonal of real dimension six.**

**Theorem (the structure of the root set).** Let $\tilde R=i\vec w$ be a value, with $\vec w$ a real vector. Then the root set of $\tilde R$ is the union, over the solutions $(\vec a,\vec b)$ of the real equation $\vec a\times\vec b=-\tfrac12\vec w$, of the complex lines

$$
\{\,\Xi_0e_0+\vec a+i\vec b\ :\ \Xi_0\in\mathbb{C}\,\},
$$

so that the root set is a complex line of roots over the solution set of one real cross-product equation. For $\vec w\neq0$ the solution set of the equation has real dimension three, and the root set has real dimension five; for $\vec w=0$ the equation is $\vec a\times\vec b=0$, whose solutions are the pairs of dependent vectors, and the root set is the cone of the diagonal of real dimension six.

*Proof.* The description of the roots is the theorem above, and the reading of its dimension is the count of the parameters: the scalar coordinate contributes two real dimensions, and the solutions of the cross-product equation in the six real coordinates of $(\vec a,\vec b)$ are cut by the three real equations of the cross product, of which the three are independent outside the degenerate locus, leaving three real dimensions. For $\vec w=0$ the equation is $\vec a\times\vec b=0$, whose solutions are the dependent pairs, a set of real dimension four, the union of the vanishing locus $\vec a=0$ and of the pairs $\vec b=\lambda\vec a$; the root set is then the cone $\{\vec\Xi=\lambda\vec v\}$ of real dimension four, together with its free central lift of real dimension two, hence the cone of the diagonal of real dimension six.

**Example (the root of $ie_3$).** For $\tilde R=ie_3$ the equation is $\vec a\times\vec b=-\tfrac12e_3$, and the pair $\vec a=e_1$, $\vec b=-\tfrac12e_2$ solves it, since $e_1\times(-\tfrac12e_2)=-\tfrac12e_3$. The element

$$
\tilde\Xi=e_1-\tfrac{i}{2}e_2
$$

is therefore a square root of $ie_3$ in the block, and the whole line of roots of $ie_3$ is obtained by adding an arbitrary complex scalar to it.

**Example (the non-roots $e_3$ and $e_0$).** The element $e_3$ is a real vector, so it is not in $i\mathbb{R}^{3}$ and it has no square root in the block; the element $e_0$ is central, and it has no square root either. The two are the elementary witnesses of the two exclusions of the criterion, and they are the elements that a naive reading would expect to be squares: $e_3$ is a unit of the vector subspace, and $e_0$ is the unit of the parent algebra. Neither is attained by the square map, and this is the content of the corollary above.

**Example (the roots of the origin).** The root set of the origin is the cone of the square-zero elements, of real dimension six, whose elements are the sums of a complex multiple of a real direction and a central element, that is the union of the complex planes $\mathbb{C}e_0\oplus\mathbb{C}\vec v$ over the real directions; the elementary roots are $e_1$ and $ie_1$, both of square zero, and the elementary non-root is the element $e_1+ie_2$, of square $-2ie_3$, which is the witness of the failure of the third power to vanish before the fourth. The cone and its two pieces are *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*.

## The Comparison with the Model Block

**In the plain product the criterion for a square root is the solvability of a quadratic equation in the central square and the root set is discrete outside the cone, while the criterion of the block is the membership of the real subspace $i\mathbb{R}^{3}$ and its root set is a complex line over a threefold family; the two criteria agree only at the origin, and the block attains a real three-dimensional set against the real six-dimensional set of the row.**

**The plain product.** In the plain product the square of an element is $\tilde\Xi\tilde\Xi=(\Xi_0^{2}-(\vec\Xi,\vec\Xi))+2\Xi_0\vec\Xi$, and the criterion for the existence of a square root of an element is the solvability of a quadratic equation in the central square $C(\tilde\Xi)=\sum_\mu \Xi_\mu^{2}$ and the scalar coordinate, with the root set discrete outside the cone of the isotropic elements; the classification is *Square Roots of a General Element in the General Plain Algebra*, and the invertibility criterion it uses is *Norm and Invertibility in the General Quaternionic Algebra*. The block has no such classification because it has no quadratic form to read: the square is not the restriction of a quadratic form, the scalar coordinate of the root is free and not determined, and the criterion is the membership of the real subspace $i\mathbb{R}^{3}$. The two criteria agree in one point only, the origin: the square roots of the origin are the cone of the square-zero elements in each of the two products, and the two cones are different sets, the cone of the block being the complex multiples of the real directions and the cone of the plain product the isotropic cone of the vector subspace.

**The row.** In the general quaternionic sesquilinear product the square roots of a general element are read with the sesquilinear pairing and the algebraic norm of the row, and the block is the antisymmetric part of that product, so that its criterion is the shadow of the criterion of the row on the antisymmetric side; the pairing of the values is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, and the two readings are compared in *The 12 Products of the Biquaternion Complex Space*. The block's criterion is the more rigid of the two: the row attains a real six-dimensional set, cut by the reality of the scalar part, by the orthogonality of the two real vectors of the vector part and by a scalar bound, while the block attains the elements of a real subspace of dimension three alone, and the loss is the price of the antisymmetrisation.

## Summary

A biquaternion has a square root in the block exactly when its scalar coordinate vanishes and its vector part is a purely imaginary real vector, that is exactly when it lies in the three real dimensional subspace $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$; the nonexistence is the whole of the central line except the origin, the whole of the real vector subspace except the origin, and the whole of the space outside the vector subspace. When the criterion holds with value $i\vec w$, the roots are the elements whose scalar coordinate is arbitrary and whose vector part is the sum $\vec a+i\vec b$ of two real vectors solving $\vec a\times\vec b=-\tfrac12\vec w$; the root set is a complex line over the solution set of that real equation, of real dimension five for a nonzero value and the cone of the diagonal, of real dimension six, for the origin. The elementary examples are the root $e_1-\tfrac{i}{2}e_2$ of $ie_3$ and the non-roots $e_3$ and $e_0$. The criterion is a subspace membership and not a quadratic equation, which is the square-root form of the absence of an algebraic norm for the block; the image of the square is the three real dimensional subspace above, and the roots of the three central values are the special case computed in the two companion articles of the block.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\diamond\tilde\Xi=\vec\Xi\times\overline{\vec\Xi}=-2i\,\vec a\times\vec b$ | the square, with $\vec\Xi=\vec a+i\vec b$ |
| $i\mathbb{R}^{3}=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | the image of the square, of real dimension three |
| $\tilde R=i\vec w$, $\vec w$ real | the criterion: the scalar coordinate vanishes and the vector part is in the image |
| $\vec a\times\vec b=-\tfrac12\vec w$ | the real equation solved by the vector part of a root |
| $\tilde\Xi=e_1-\tfrac{i}{2}e_2$ | the root of $ie_3$ |
| $e_3$, $e_0$ | the non-roots of the vector subspace and of the central line |
| $\Xi_0\in\mathbb{C}$ free | the complex line of the root set |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, for the square root of an element and the root of a central value, for a general product.
- *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Sesqualgebra*, for the special case of the value $+1$ and for the idempotents of the block.
- *Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*, for the special case of the value $0$, for the cone of the diagonal and for the nilpotents.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, for the diagonal, its cone and its image.
- *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra*, for the absence of the algebraic norm which makes the criterion linear instead of quadratic.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the pairing of the values.
- *Square Roots of a General Element in the General Plain Algebra*, for the model block, where the criterion is quadratic and the root set is discrete outside the cone.
