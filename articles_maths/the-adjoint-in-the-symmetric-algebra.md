# __The Adjoint in the Symmetric Algebra__

## Introduction

The symmetric algebra $A = \operatorname{Sym}(M)$ of a free module of finite rank carries the **trace form**, the coefficient pairing $\langle u,v\rangle$ that reads off the diagonal term of the product; in a basis $x_1,\dots,x_n$ with the dual differential operators $\partial_1,\dots,\partial_n$ it is the **apolar pairing** $\langle u,v\rangle = v(\partial)u|_{0}$. With respect to it every operator has an adjoint, and the article computes the adjoints of the **multiplication operators** of the symmetric algebra. The result is that the adjoint of the multiplication by $x_i$ is the derivative $\partial_i$,

$$
\langle x_i u, v\rangle = \langle u, \partial_i v\rangle ,
$$

so the adjoint of a multiplication is a **differential operator with constant coefficients**, the polarisation operator $P_u = u(\partial)$ of *The Polarisation Operator*, and not another multiplication; consequently the only self-adjoint multiplications are the **scalar** ones. This is the specific behaviour of the trace form, and it is the reason the polarisation operator enters the operator theory of the symmetric algebra: the multiplications and the polarisation operators are mutual adjoints, and the involution they define on the endomorphism algebra is the transpose.

The article defines the trace form, proves that it is symmetric, non-degenerate and graded, computes the adjoint of a multiplication as the polarisation operator, identifies the self-adjoint multiplications as the scalar ones, and describes the induced transpose involution on the endomorphisms of the symmetric algebra with its self-adjoint part and its unitary group. It compares the result with the multiplication operators of *Involutions of the Multiplication Operators*, *Adjoints in a Commutative Involutive Algebra* and *The Involution on the Multiplication Operators*, where the pairing is $\sigma$-sesquilinear and the adjoint of $L_a$ is again a multiplication; the difference is exactly the difference between the trace form and a sesquilinear form, and the article marks it. The article assumes *The Symmetric Algebra with an Involution* and *The Symmetric and Exterior Powers* for the algebra and its grading, *The Polarisation Operator* for $P_u$ and its properties, *The Adjoint of an Endomorphism* for the adjoint with respect to a pairing, and *Involutive Bilinear Algebras* for the involution of the endomorphism algebra. The signed variants are *The Signed Adjoint Sandwich*, *The Signed Adjoint of the Reflection* and *The Signed Adjoint of the Left Multiplication*, later in this group. Throughout, $R$ is a commutative ring with identity in which all the factorials are invertible (for instance a field of characteristic zero), $M$ is a free $R$-module of rank $n$ with basis $x_1,\dots,x_n$, $A = \operatorname{Sym}(M)$ is its symmetric algebra, $\partial_i$ is the derivative dual to $x_i$, and $\langle\cdot,\cdot\rangle$ is the trace form; no norm, distance, positivity or operator spectrum occurs.

## The Symmetric Algebra and the Trace Form

### The Trace Form

**Definition.** The **trace form** on $A = \operatorname{Sym}(M)$ is the $R$-bilinear map

$$
\langle\cdot,\cdot\rangle : A\times A\to R, \qquad \langle u,v\rangle = \bigl(v(\partial)\,u\bigr)\big|_{x=0},
$$

where $v(\partial)$ is the differential operator with constant coefficients obtained by replacing $x_i$ by $\partial_i$ in $v$, and the index $0$ means the constant term. On the monomials it is the apolar pairing

$$
\langle x^{a}, x^{b}\rangle = a!\,\delta_{a,b}, \qquad a! = a_1!\cdots a_n! .
$$

**Theorem.** The trace form is $R$-bilinear, symmetric, non-degenerate and graded: $\langle \operatorname{Sym}^k(M), \operatorname{Sym}^j(M)\rangle = 0$ for $k\ne j$, and on $\operatorname{Sym}^k(M)$ it is a non-degenerate pairing.

*Proof.* Bilinearity is the bilinearity of the coefficient extraction; symmetry is the commutativity of the differential operators with constant coefficients, $\partial^a\partial^b = \partial^{a+b} = \partial^b\partial^a$; the monomial formula is immediate; the pairing is diagonal in the monomial bases with the invertible coefficients $a!$, hence non-degenerate on each finite free homogeneous piece and graded. $\square$

**Proposition (invariance under the induced involution).** Let $\sigma_M$ be an $R$-linear involution of $M$ preserving the trace form, $\langle \sigma_M(x),\sigma_M(y)\rangle = \langle x,y\rangle$, and let $\sigma$ be the induced involution of $A$. Then $\sigma$ preserves the trace form, $\langle \sigma(u),\sigma(v)\rangle = \langle u,v\rangle$, and the trace form is compatible with the multiplication of *The Symmetric Algebra with an Involution*.

*Proof.* The induced involution is multiplicative and acts by $\sigma_M$ on the generators; applied to the monomials, the invariance follows from the invariance of the pairing on $M$ extended multiplicatively. $\square$

## The Adjoint of a Multiplication

### The Multiplication by a Generator

**Theorem.** For every generator $x_i$ the adjoint of the multiplication $L_{x_i}$ with respect to the trace form is the derivative $\partial_i$:

$$
L_{x_i}^{\dagger} = \partial_i , \qquad \text{that is} \qquad \langle x_i u, v\rangle = \langle u, \partial_i v\rangle .
$$

*Proof.* On the monomials, $\langle x_i x^a, x^b\rangle = \langle x^{a+e_i}, x^b\rangle = (a+e_i)!\,\delta_{a+e_i,b}$ and $\langle x^a, \partial_i x^b\rangle = b_i\langle x^a,x^{b-e_i}\rangle = b_i\,a!\,\delta_{a,b-e_i}$; the two agree because $a+e_i = b$ gives $b_i = a_i+1$ and $(a+e_i)! = (a_i+1)a!$. Hence the two operators are adjoint. $\square$

### The Multiplication by a General Element

**Theorem.** For every $u \in A$ the adjoint of the multiplication $L_u$ with respect to the trace form is the **polarisation operator** $P_u = u(\partial)$ of *The Polarisation Operator*:

$$
L_u^{\dagger} = u(\partial) = P_u , \qquad \text{that is} \qquad \langle u w, v\rangle = \langle w, u(\partial)v\rangle .
$$

*Proof.* Both sides are additive in $u$, and for a monomial $u = x^a$ the operator $u(\partial) = \partial^a$ is the composite $\partial^{a} = \partial_1^{a_1}\cdots\partial_n^{a_n}$; the relation $\langle x_iw,\cdot\rangle = \langle w,\partial_i\cdot\rangle$ composes to $\langle u w,v\rangle = \langle w, u(\partial)v\rangle$. $\square$

**Corollary (the self-adjoint multiplications).** A multiplication $L_u$ is self-adjoint with respect to the trace form exactly when $u$ is a scalar: $L_u^{\dagger} = L_u$ iff $u \in R$ (the constants of the symmetric algebra).

*Proof.* $L_u^{\dagger} = u(\partial)$ and $L_u$ is a multiplication of degree $\deg u$, while $u(\partial)$ lowers the degree by $\deg u$; the two operators are equal only when $\deg u = 0$, and then $u(\partial) = u$ is the scalar multiplication. $\square$

**Corollary (the mutual adjointness).** The multiplication $L_u$ and the polarisation operator $P_u$ are mutual adjoints, $L_u^{\dagger} = P_u$ and $P_u^{\dagger} = L_u$; the map $u\mapsto (L_u, P_u)$ is an isomorphism of $A$ onto a pair of adjoint families of operators.

*Proof.* $(L_u^{\dagger})^{\dagger} = L_u$ by the involutivity of the adjoint, and $L_u^{\dagger} = P_u$, so $P_u^{\dagger} = L_u$. $\square$

## The Self-Adjoint Operators and the Induced Involution

**Theorem.** The assignment $F\mapsto F^{\dagger}$ is an involution of the endomorphism algebra $\operatorname{End}_R(A)$, the **transpose involution** with respect to the trace form; the self-adjoint operators form a Jordan algebra under the symmetrised product and the skew-adjoint operators a Lie algebra under the commutator, with the decomposition into the two when $2$ is invertible; the unitary operators, those with $F^{\dagger}F = FF^{\dagger} = 1$, form a group.

*Proof.* This is *The Adjoint of an Endomorphism* together with *Involutive Bilinear Algebras*, read on the trace form. $\square$

**Proposition.** The polarisation operators form the image of the symmetric algebra under the adjoint of the multiplication map, $A\to\operatorname{End}_R(A)$, $u\mapsto P_u = L_u^{\dagger}$; they commute, $P_uP_v = P_{uv}$, because the differential operators with constant coefficients commute, and they are the operators of *The Polarisation Operator* written as the adjoints of the multiplications.

*Proof.* $P_uP_v = u(\partial)v(\partial) = (uv)(\partial) = P_{uv}$, as differential operators with constant coefficients commute. $\square$

## Examples

**Example (one variable).** For $M = Rx$, $A = R[x]$, the trace form is $\langle x^a, x^b\rangle = a!\,\delta_{a,b}$; the adjoint of $L_x$ is $\partial_x$, so $L_x^{\dagger} = \partial_x$ and $L_x$ is not self-adjoint; $L_x + \partial_x$ is not a multiplication, and its square is not either, since $L_x\partial_x = \partial_x L_x+\mathrm{id}$ by $[\partial_x,x] = 1$. The only self-adjoint multiplications are the constants $L_\lambda$.

**Example (two variables).** For $M = Rx_1\oplus Rx_2$, $A = R[x_1,x_2]$, the trace form is $\langle x_1^{a_1}x_2^{a_2}, x_1^{b_1}x_2^{b_2}\rangle = a_1!a_2!\,\delta_{a,b}$; the adjoint of $L_{x_1}$ is $\partial_1$, the adjoint of $L_{x_1x_2}$ is $\partial_1\partial_2$, and the adjoint of $L_{x_1^2+x_2^2}$ is $\partial_1^2+\partial_2^2$, the polarisation operator of the invariant $x_1^2+x_2^2$. The scalar multiplications are the only self-adjoint multiplications.

## Summary

The **trace form** on the symmetric algebra $A = \operatorname{Sym}(M)$ of a free module of finite rank is the apolar pairing $\langle u,v\rangle = v(\partial)u|_{0}$, symmetric, non-degenerate and graded. With respect to it the adjoint of the multiplication by a generator is the derivative, $L_{x_i}^{\dagger} = \partial_i$, and the adjoint of a general multiplication is the **polarisation operator**, $L_u^{\dagger} = u(\partial) = P_u$; the multiplication and the polarisation operator are mutual adjoints, and the polarisation operators commute as the differential operators with constant coefficients do. The only **self-adjoint** multiplications are the **scalar** ones, because the multiplication raises the degree and the polarisation operator lowers it. The assignment $F\mapsto F^{\dagger}$ is the **transpose involution** of the endomorphism algebra, whose self-adjoint operators form a Jordan algebra, whose skew-adjoint operators form a Lie algebra and whose unitary operators form a group. The trace form thus differs from the $\sigma$-sesquilinear pairings of the preceding articles, where the adjoint of $L_a$ is the multiplication $L_{\sigma(a)}$. No norm, distance, positivity or operator spectrum occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A = \operatorname{Sym}(M)$, $M$ free of rank $n$ | Symmetric algebra |
| $\langle u,v\rangle = v(\partial)u|_{0}$ | Trace form (apolar pairing) |
| $\langle x^a,x^b\rangle = a!\,\delta_{a,b}$ | Value on the monomials |
| $L_{x_i}^{\dagger} = \partial_i$ | Adjoint of a generator multiplication |
| $L_u^{\dagger} = u(\partial) = P_u$ | Adjoint of a multiplication $=$ polarisation operator |
| $L_u^{\dagger} = L_u \iff u\in R$ | Self-adjoint multiplications are the scalars |
| $F\mapsto F^{\dagger}$ | Transpose involution of $\operatorname{End}_R(A)$ |

## Further Reading

- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the apolar pairing, the symmetric algebra and the duality.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the symmetric algebra, the polynomial algebra and the divided powers.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the adjoint involution and the pairings.
- Igor Shafarevich and Alexander Kostrikin, *Linear Algebra and Geometry* (Gordon and Breach, 1989), for the polarisation, the apolar form and the symmetric powers.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the adjoints and the endomorphism algebras.
