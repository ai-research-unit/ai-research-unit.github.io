# __Association and the Transpose on the General Plain Algebra__

## Introduction

The plain product pairs with the scalar functional into one bilinear form, the **plain form** $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$, and that form has a transpose calculus: every real-linear operator $T$ of $\mathbb{H}$ has a transpose $T^{\sim}$ defined by $\mathrm B(T\tilde p,\tilde q)=\mathrm B(\tilde p,T^{\sim}\tilde q)$, and the transposes of the one- and two-sided multiplications are computable in closed form. The two products and the two forms are owned by *The 6 Products of the Quaternion Real Space* and *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, above this article in this category; the operators themselves are *Two-Sided Operators on the General Plain Algebra of Quaternions*, below this article in this category, and *One-Sided Operators on the General Plain Algebra of Quaternions*, below this article in this category; the enveloping algebra is *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, below this article in this category.

The form is symmetric and indefinite of signature $(1,3)$. It is not the positive definite coordinate pairing, and the whole of the calculus below is the bookkeeping of that gap: the Gram matrix is the diagonal matrix of the signature, and the transpose of an operator is the operator's matrix conjugated by it.

## The Plain Form

**Definition.** The **plain form** is $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$, the scalar part of the plain product, a bilinear form on $\mathbb{H}$.

**Proposition.** $\mathrm B$ is symmetric, non-degenerate, and indefinite of signature $(1,3)$; in the basis $e_0,e_1,e_2,e_3$ its Gram matrix is

$$
D=\operatorname{diag}(1,-1,-1,-1).
$$

*Proof.* Symmetry is the identity $\mathrm{Sc}(\tilde p\tilde q)=\mathrm{Sc}(\tilde q\tilde p)$, read from the coordinate formula: the scalar part of a product is $p_0q_0-p_1q_1-p_2q_2-p_3q_3$, which is unchanged when the two factors are exchanged. Non-degeneracy and the Gram matrix are the table of the scalar parts of the sixteen products: $\mathrm B(e_0,e_0)=1$, $\mathrm B(e_k,e_k)=-1$, and $\mathrm B(e_\mu,e_\nu)=0$ for $\mu\neq\nu$.

**Corollary.** $\mathrm B$ is the polar form of the quadratic form $Q(\tilde q)=\mathrm{Sc}(\tilde q^2)=q_0^2-q_1^2-q_2^2-q_3^2$, and the associated quadratic form is indefinite.

*Proof.* $\mathrm B(\tilde p,\tilde q)=\tfrac12(Q(\tilde p+\tilde q)-Q(\tilde p)-Q(\tilde q))$ by bilinearity, and $D$ has one positive and three negative diagonal entries.

## The Association Functional

**Definition.** The **association functional** is the trilinear form $A(\tilde p,\tilde q,\tilde r)=\mathrm{Sc}(\tilde p\tilde q\tilde r)$.

**Theorem (cyclic invariance).** $A(\tilde p,\tilde q,\tilde r)=A(\tilde q,\tilde r,\tilde p)=A(\tilde r,\tilde p,\tilde q)$.

*Proof.* Apply the symmetry of the form, $\mathrm{Sc}(\tilde x\tilde y)=\mathrm{Sc}(\tilde y\tilde x)$, to the pair $\tilde x=\tilde p\tilde q$, $\tilde y=\tilde r$: $\mathrm{Sc}(\tilde p\tilde q\tilde r)=\mathrm{Sc}(\tilde r\tilde p\tilde q)$, which is the cyclic shift; the second is the shift of the first.

**Corollary (the association is immaterial).** $A$ is unchanged when the two multiplications are associated in the other order, $A(\tilde p,\tilde q,\tilde r)=\mathrm{Sc}((\tilde p\tilde q)\tilde r)=\mathrm{Sc}(\tilde p(\tilde q\tilde r))$, by associativity alone; cyclic invariance is the additional statement that the two arguments can be moved without changing the value.

**Definition.** The association functional defines the **sandwich operators** $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$, and $A(\tilde p,\tilde q,\tilde r)=\mathrm B(L_{\tilde p}R_{\tilde r}\tilde q,e_0)$ reads the functional through one of them.

## The Transposes of the One-Sided Operators

**Definition.** For a real-linear operator $T$ of $\mathbb{H}$ the **transpose** $T^{\sim}$ is the operator with $\mathrm B(T\tilde p,\tilde q)=\mathrm B(\tilde p,T^{\sim}\tilde q)$ for all $\tilde p,\tilde q$. Non-degeneracy of $\mathrm B$ makes $T^{\sim}$ unique, and $T\mapsto T^{\sim}$ is an anti-automorphism of the operator algebra.

**Theorem.** $L_{\tilde a}^{\sim}=R_{\tilde a}$ and $R_{\tilde b}^{\sim}=L_{\tilde b}$.

*Proof.* $\mathrm B(L_{\tilde a}\tilde p,\tilde q)=\mathrm{Sc}(\tilde a\tilde p\tilde q)$ and $\mathrm B(\tilde p,R_{\tilde a}\tilde q)=\mathrm{Sc}(\tilde p\tilde q\tilde a)$, equal by cyclic invariance of the association functional; hence $L_{\tilde a}^{\sim}=R_{\tilde a}$, and the second is the mirror with the two sides swapped.

**Corollary.** $L_{\tilde a}$ is self-transpose exactly when $\tilde a$ is central; the self-transpose left multiplications are the scalar ones.

*Proof.* $L_{\tilde a}=R_{\tilde a}$ exactly when $\tilde a$ commutes with every element, that is, by the centre theorem, when $\tilde a\in\mathbb{R}e_0$.

## The Transpose of a Two-Sided Operator

**Theorem.** For the sandwich $T_{\tilde a,\tilde b}=L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$,

$$
T_{\tilde a,\tilde b}^{\sim}=L_{\tilde b}R_{\tilde a}=T_{\tilde b,\tilde a}.
$$

*Proof.* The transpose is an anti-automorphism, $(UV)^{\sim}=V^{\sim}U^{\sim}$, so $T_{\tilde a,\tilde b}^{\sim}=(L_{\tilde a}R_{\tilde b})^{\sim}=R_{\tilde b}^{\sim}L_{\tilde a}^{\sim}=L_{\tilde b}R_{\tilde a}$, which is $T_{\tilde b,\tilde a}$.

**Corollary.** The sandwich is self-transpose exactly when $\tilde b\in\mathbb{R}\tilde a$ or $\tilde a\in\mathbb{R}\tilde b$.

*Proof.* The equality $L_{\tilde a}R_{\tilde b}=L_{\tilde b}R_{\tilde a}$ says $\tilde a\tilde q\tilde b=\tilde b\tilde q\tilde a$ for every $\tilde q$. At $\tilde q=e_0$ it gives $\tilde a\tilde b=\tilde b\tilde a$, so $\tilde b$ commutes with $\tilde a$; if $\tilde b=\mu\tilde a$ for some real $\mu$ the two sides are equal, which is the sufficiency. Conversely, either $\tilde a$ is central, and then the identity reads $\tilde q\tilde a\tilde b=\tilde b\tilde q\tilde a$, that is $\tilde q\tilde c=\tilde c\tilde q$ with $\tilde c=\tilde a\tilde b$ central because $\tilde a$ is and $\tilde b$ commutes with it, so $\tilde b$ is central too and $\tilde b\in\mathbb{R}\tilde a$; or $\tilde a$ is not central, its commutant is the plane $\mathbb{R}e_0+\mathbb{R}\tilde a$, and $\tilde b=\lambda+\mu\tilde a$ gives $\tilde a\tilde q\tilde b-\tilde b\tilde q\tilde a=\lambda(\tilde a\tilde q-\tilde q\tilde a)$, which vanishes for all $\tilde q$ only if $\lambda=0$, that is $\tilde b\in\mathbb{R}\tilde a$. The degenerate cases $\tilde a=0$ or $\tilde b=0$ are included, both sides being $0$.

**Theorem (the natural sign is self-transpose).** The operator $\natural:\tilde q\mapsto\tilde q^{\natural}$ satisfies $\natural^{\sim}=\natural$.

*Proof.* $\mathrm B(\tilde p^{\natural},\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=\sum_\mu p_\mu q_\mu$ and $\mathrm B(\tilde p,\tilde q^{\natural})=\mathrm{Sc}(\tilde p\tilde q^{\natural})=\sum_\mu p_\mu q_\mu$; the two agree for all $\tilde p,\tilde q$, so the operator is self-transpose. The formula displays the coordinate pairing as the plain form read through the natural sign in either slot.

## The Matrix Formula for the Transpose

**Theorem.** Let $T$ be real-linear with matrix $G$ in the basis $e_0,e_1,e_2,e_3$ and let $D=\operatorname{diag}(1,-1,-1,-1)$. Then $T^{\sim}$ has matrix

$$
G^{\sim}=D\,G^{\mathsf T}D .
$$

*Proof.* For all $\tilde p,\tilde q$, $\mathrm B(T\tilde p,\tilde q)=(Gp)^{\mathsf T}Dq=p^{\mathsf T}G^{\mathsf T}Dq$ and $\mathrm B(\tilde p,T^{\sim}\tilde q)=p^{\mathsf T}D(G^{\sim}q)=p^{\mathsf T}DG^{\sim}q$, where $p,q$ are the coordinate columns; equating the two for all $p,q$ gives $G^{\mathsf T}D=DG^{\sim}$, that is $G^{\sim}=D^{-1}G^{\mathsf T}D=D\,G^{\mathsf T}D$ because $D^{-1}=D= D^{\mathsf T}$.

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

**Theorem.** The plain form read through the natural sign in either slot is the positive definite coordinate pairing:

$$
\mathrm B(\tilde p^{\natural},\tilde q)=\mathrm B(\tilde p,\tilde q^{\natural})=\sum_{\mu}p_\mu q_\mu=\mathrm{Sc}(\tilde p^{\natural}\tilde q).
$$

*Proof.* $\tilde p^{\natural}\tilde q=\sum_\mu p_\mu q_\mu+\text{(a vector part)}$ and $\tilde p\tilde q^{\natural}$ likewise; the scalar part is the sum of the coordinate products, the vector parts being sums of the basis vectors without a scalar component.

**Corollary.** The natural sign is the adjoint of the identity of the plain form: it carries the indefinite form to the positive definite coordinate one, and its self-transposeness is the statement that the two pairings agree.

## Summary

The plain form $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ is symmetric, non-degenerate and indefinite of signature $(1,3)$, with Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ and polar quadratic form $\mathrm{Sc}(\tilde q^2)=q_0^2-q_1^2-q_2^2-q_3^2$. The association functional $\mathrm{Sc}(\tilde p\tilde q\tilde r)$ is cyclically invariant, and the association of the two multiplications does not change it. The transpose of a real-linear operator is $G^{\sim}=D\,G^{\mathsf T}D$ in matrix form, and on the elementary operators it is $L_{\tilde a}^{\sim}=R_{\tilde a}$, $R_{\tilde b}^{\sim}=L_{\tilde b}$, $(L_{\tilde a}R_{\tilde b})^{\sim}=L_{\tilde b}R_{\tilde a}$ and $\natural^{\sim}=\natural$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ | The plain form |
| $A(\tilde p,\tilde q,\tilde r)=\mathrm{Sc}(\tilde p\tilde q\tilde r)$ | The association functional |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of $\mathrm B$ |
| $T^{\sim}$ | Transpose of the operator $T$ |
| $L_{\tilde a},R_{\tilde b}$ | Left and right multiplications |
| $\natural$ | The natural sign, the quaternion conjugation |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for bilinear forms on finite-dimensional algebras and the transpose calculus.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for bilinear forms, their Gram matrices and their signature.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the scalar-part pairing and the conjugation of the quaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the cyclic invariance of the scalar triple product.
