# __Association and the Transpose on the Quaternion Algebra__

## Introduction

The quaternion product pairs with the scalar functional into one bilinear form, the **product form** $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$, and that form has a transpose calculus: every real-linear operator $T$ of $\mathbb{H}$ has a transpose $T^{\sim}$ defined by $\langle T\tilde q_1,\tilde q_2\rangle=\langle\tilde q_1,T^{\sim}\tilde q_2\rangle$, and the transposes of the one- and two-sided multiplications are computable in closed form. The form of the quaternion product is read in this article; the operators themselves are *Two-Sided Operators on the Quaternion Algebra*, below this article in this category, and *One-Sided Operators on the Quaternion Algebra*, below this article in this category; the enveloping algebra is *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

The form is symmetric and indefinite of signature $(1,3)$. It is not the positive definite coordinate pairing, and the whole of the calculus below is the bookkeeping of that gap: the Gram matrix is the diagonal matrix of the signature, and the transpose of an operator is the operator's matrix conjugated by it.

## The Plain Form

**Definition.** The **product form** is $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$, the scalar part of the quaternion product, a bilinear form on $\mathbb{H}$.

**Proposition.** $\mathrm B$ is symmetric, non-degenerate, and indefinite of signature $(1,3)$; in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ its Gram matrix is

$$
D=\operatorname{diag}(1,-1,-1,-1).
$$

*Proof.* Symmetry is the identity $\mathrm{Sc}(\tilde q_1\tilde q_2)=\mathrm{Sc}(\tilde q_2\tilde q_1)$, read from the coordinate formula: the scalar part of a product is $q_{1t}q_{2t}-q_{1x}q_{2x}-q_{1y}q_{2y}-q_{1z}q_{2z}$, which is unchanged when the two factors are exchanged. Non-degeneracy and the Gram matrix are the table of the scalar parts of the sixteen products: $\mathrm B(e_t,e_t)=1$, $\mathrm B(\vec e_\mu,\vec e_\mu)=-1$, and $\mathrm B(e_\mu,e_\nu)=0$ for $\mu\neq\nu$.

**Corollary.** $\mathrm B$ is the polar form of the quadratic form $\mathfrak{Q}(\tilde q)=\mathrm{Sc}(\tilde q^2)=q_t^2-q_x^2-q_y^2-q_z^2$, and the associated quadratic form is indefinite.

*Proof.* $\langle\tilde q_1,\tilde q_2\rangle=\tfrac12(\mathfrak{Q}(\tilde q_1+\tilde q_2)-\mathfrak{Q}(\tilde q_1)-\mathfrak{Q}(\tilde q_2))$ by bilinearity, and $D$ has one positive and three negative diagonal entries.

## The Association Functional

**Definition.** The **association functional** is the trilinear form $A(\tilde q_1,\tilde q_2,\tilde q_3)=\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)$.

**Theorem (cyclic invariance).** $A(\tilde q_1,\tilde q_2,\tilde q_3)=A(\tilde q_2,\tilde q_3,\tilde q_1)=A(\tilde q_3,\tilde q_1,\tilde q_2)$.

*Proof.* Apply the symmetry of the form, $\mathrm{Sc}(\tilde x\tilde y)=\mathrm{Sc}(\tilde y\tilde x)$, to the pair $\tilde x=\tilde q_1\tilde q_2$, $\tilde y=\tilde q_3$: $\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)=\mathrm{Sc}(\tilde q_3\tilde q_1\tilde q_2)$, which is the cyclic shift; the second is the shift of the first.

**Corollary (the association is immaterial).** $A$ is unchanged when the two multiplications are associated in the other order, $A(\tilde q_1,\tilde q_2,\tilde q_3)=\mathrm{Sc}((\tilde q_1\tilde q_2)\tilde q_3)=\mathrm{Sc}(\tilde q_1(\tilde q_2\tilde q_3))$, by associativity alone; cyclic invariance is the additional statement that the two arguments can be moved without changing the value.

**Definition.** The association functional defines the **sandwich operators** $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$, and $A(\tilde q_1,\tilde q_2,\tilde q_3)=\mathrm B(L_{\tilde q_1}R_{\tilde q_3}\tilde q_2,e_t)$ reads the functional through one of them.

## The Transposes of the One-Sided Operators

**Definition.** For a real-linear operator $T$ of $\mathbb{H}$ the **transpose** $T^{\sim}$ is the operator with $\langle T\tilde q_1,\tilde q_2\rangle=\langle\tilde q_1,T^{\sim}\tilde q_2\rangle$ for all $\tilde q_1,\tilde q_2$. Non-degeneracy of $\mathrm B$ makes $T^{\sim}$ unique, and $T\mapsto T^{\sim}$ is an anti-automorphism of the operator algebra.

**Theorem.** $L_{\tilde a}^{\sim}=R_{\tilde a}$ and $R_{\tilde b}^{\sim}=L_{\tilde b}$.

*Proof.* $\langle L_{\tilde a}\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde a\tilde q_1\tilde q_2)$ and $\langle\tilde q_1,R_{\tilde a}\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2\tilde a)$, equal by cyclic invariance of the association functional; hence $L_{\tilde a}^{\sim}=R_{\tilde a}$, and the second is the mirror with the two sides swapped.

**Corollary.** $L_{\tilde a}$ is self-transpose exactly when $\tilde a$ is central; the self-transpose left multiplications are the scalar ones.

*Proof.* $L_{\tilde a}=R_{\tilde a}$ exactly when $\tilde a$ commutes with every element, that is, by the centre theorem, when $\tilde a\in\mathbb{R}e_t$.

## The Transpose of a Two-Sided Operator

**Theorem.** For the sandwich $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$,

$$
T_{\tilde a,\tilde b}^{\sim}=L_{\tilde b}R_{\tilde a}=T_{\tilde b,\tilde a}.
$$

*Proof.* The transpose is an anti-automorphism, $(\tilde q_1\tilde q_2)^{\sim}=\tilde q_2^{\sim}\tilde q_1^{\sim}$, so $T_{\tilde a,\tilde b}^{\sim}=(L_{\tilde a}R_{\tilde b})^{\sim}=R_{\tilde b}^{\sim}L_{\tilde a}^{\sim}=L_{\tilde b}R_{\tilde a}$, which is $T_{\tilde b,\tilde a}$.

**Corollary.** The sandwich is self-transpose exactly when $\tilde b\in\mathbb{R}\tilde a$ or $\tilde a\in\mathbb{R}\tilde b$.

*Proof.* The equality $L_{\tilde a}R_{\tilde b}=L_{\tilde b}R_{\tilde a}$ says $\tilde a\tilde q\tilde b=\tilde b\tilde q\tilde a$ for every $\tilde q$. At $\tilde q=e_t$ it gives $\tilde a\tilde b=\tilde b\tilde a$, so $\tilde b$ commutes with $\tilde a$; if $\tilde b=\mu\tilde a$ for some real $\mu$ the two sides are equal, which is the sufficiency. Conversely, either $\tilde a$ is central, and then the identity reads $\tilde q\tilde a\tilde b=\tilde b\tilde q\tilde a$, that is $\tilde q\tilde c=\tilde c\tilde q$ with $\tilde c=\tilde a\tilde b$ central because $\tilde a$ is and $\tilde b$ commutes with it, so $\tilde b$ is central too and $\tilde b\in\mathbb{R}\tilde a$; or $\tilde a$ is not central, its commutant is the plane $\mathbb{R}e_t+\mathbb{R}\tilde a$, and $\tilde b=\lambda+\mu\tilde a$ gives $\tilde a\tilde q\tilde b-\tilde b\tilde q\tilde a=\lambda(\tilde a\tilde q-\tilde q\tilde a)$, which vanishes for all $\tilde q$ only if $\lambda=0$, that is $\tilde b\in\mathbb{R}\tilde a$. The degenerate cases $\tilde a=0$ or $\tilde b=0$ are included, both sides being $0$.

**Theorem (the natural sign is self-transpose).** The operator $\natural:\tilde q\mapsto\tilde q^{\natural}$ satisfies $\natural^{\sim}=\natural$.

*Proof.* $\langle\tilde q_1^{\natural},\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=\sum_\mu q_{1\mu} q_{2\mu}$ and $\langle\tilde q_1,\tilde q_2^{\natural}\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})=\sum_\mu q_{1\mu} q_{2\mu}$; the two agree for all $\tilde q_1,\tilde q_2$, so the operator is self-transpose. The formula displays the coordinate pairing as the product form read through the natural sign in either slot.

## The Matrix Formula for the Transpose

**Theorem.** Let $T$ be real-linear with matrix $G$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and let $D=\operatorname{diag}(1,-1,-1,-1)$. Then $T^{\sim}$ has matrix

$$
G^{\sim}=D\,G^{\mathsf T}D.
$$

*Proof.* For all $\tilde q_1,\tilde q_2$, $\langle T\tilde q_1,\tilde q_2\rangle=(Gq_1)^{\mathsf T}Dq_2=q_1^{\mathsf T}G^{\mathsf T}Dq_2$ and $\langle\tilde q_1,T^{\sim}\tilde q_2\rangle=q_1^{\mathsf T}D(G^{\sim}q_2)=q_1^{\mathsf T}DG^{\sim}q_2$, where $q_1,q_2$ are the coordinate columns; equating the two for all $q_1,q_2$ gives $G^{\mathsf T}D=DG^{\sim}$, that is $G^{\sim}=D^{-1}G^{\mathsf T}D=D\,G^{\mathsf T}D$ because $D^{-1}=D= D^{\mathsf T}$.

**Corollary.** The transpose matrix is the matrix transpose conjugated by the signature matrix; in particular the transposes of $L_{\tilde a}$ and $R_{\tilde a}$ are obtained by $L_{\tilde a}^{\sim}=D\,L_{\tilde a}^{\mathsf T}D=R_{\tilde a}$ and $R_{\tilde a}^{\sim}=D\,R_{\tilde a}^{\mathsf T}D=L_{\tilde a}$.

*Proof.* The formula applied to the matrix of each operator, with the identifications of the theorem above.

**Corollary (the operator table).** The transposes of the elementary operators are

| Operator | Transpose |
|---|---|
| $L_{\tilde a}$ | $R_{\tilde a}$ |
| $R_{\tilde b}$ | $L_{\tilde b}$ |
| $L_{\tilde a}R_{\tilde b}$ | $L_{\tilde b}R_{\tilde a}$ |
| $\natural$ | $\natural$ |

*Proof.* The four statements above.

## The Identity against the Quaternion Adjoint

**Theorem.** The product form read through the natural sign in either slot is the positive definite coordinate pairing:

$$
\langle\tilde q_1^{\natural},\tilde q_2\rangle=\langle\tilde q_1,\tilde q_2^{\natural}\rangle=\sum_{\mu}q_{1\mu} q_{2\mu}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2).
$$

*Proof.* $\tilde q_1^{\natural}\tilde q_2=\sum_\mu q_{1\mu} q_{2\mu}+\text{(a vector part)}$ and $\tilde q_1\tilde q_2^{\natural}$ likewise; the scalar part is the sum of the coordinate products, the vector parts being sums of the basis vectors without a scalar component.

**Corollary.** The natural sign is the adjoint of the identity of the product form: it carries the indefinite form to the positive definite coordinate one, and its self-transposeness is the statement that the two pairings agree.

## Summary

The product form $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ is symmetric, non-degenerate and indefinite of signature $(1,3)$, with Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ and polar quadratic form $\mathrm{Sc}(\tilde q^2)=q_t^2-q_x^2-q_y^2-q_z^2$. The association functional $\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)$ is cyclically invariant, and the association of the two multiplications does not change it. The transpose of a real-linear operator is $G^{\sim}=D\,G^{\mathsf T}D$ in matrix form, and on the elementary operators it is $L_{\tilde a}^{\sim}=R_{\tilde a}$, $R_{\tilde b}^{\sim}=L_{\tilde b}$, $(L_{\tilde a}R_{\tilde b})^{\sim}=L_{\tilde b}R_{\tilde a}$ and $\natural^{\sim}=\natural$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | The product form |
| $A(\tilde q_1,\tilde q_2,\tilde q_3)=\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)$ | The association functional |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of $\mathrm B$ |
| $T^{\sim}$ | Transpose of the operator $T$ |
| $L_{\tilde a},R_{\tilde b}$ | Left and right multiplications |
| $\natural$ | The natural sign, the quaternion conjugation |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for bilinear forms on finite-dimensional algebras and the transpose calculus.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for bilinear forms, their Gram matrices and their signature.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the scalar-part pairing and the conjugation of the quaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the cyclic invariance of the scalar triple product.
