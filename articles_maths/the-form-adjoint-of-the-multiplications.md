# __The Form-Adjoint of the Multiplications__

## Introduction

The compatibility of *Sesqualgebras with a Form* is the statement that the involution of the algebra computes the adjoint of the multiplications, and this article makes that statement explicit. The left multiplication by $x$ has for adjoint the left multiplication by $x^{*}$, and the **sandwich** $\Theta_{x}(y) = xyx^{*}$ has for adjoint the sandwich by $x^{*}$:

$$
L_{x}^{*} = L_{x^{*}}, \qquad \Theta_{x}^{*} = \Theta_{x^{*}} .
$$

The two identities are what make the objects of the category operator-theoretic: the algebra acts on itself by operators whose adjoints are given by the involution alone, with no Gram matrix, no basis and no completion. The right multiplication is subtler and does not obey the same rule: the identity $R_{x}^{*} = R_{x^{*}}$ is *not* a consequence of the compatibility, it is exactly the third identity refused in *Sesqualgebras with a Form*, and it holds for the trace form $\tau(xy^{*})$ while it fails for the compatible form $\tau(xGy^{*})$ with $G = \operatorname{diag}(1,-1)$. What does hold always is $R_{x}^{*} = R_{x^{t}}$, the right multiplication by the **transpose** of $x$ for the form, and the present article states the three facts separately.

The operators themselves, their sums, products and adjoints, are *The Form-Adjoint of an Operator*; the sandwich $\Theta_{x}$ and its role in the conjugation of the group are *The Inner Conjugation on the Two-Sided Operators* of the two-sided groups of this category; the one-sided operators are *One-Sided Operators on a Clifford Algebra* and the articles of the one-sided groups; the spectral and the bounded reading is Part II, *The Adjoint of the Left and the Right Multiplication* and *The Adjoint of the Sandwich on a Hermitian Algebra*. Throughout, $(A,*,h)$ is a sesqualgebra with a form with $h$ nonsingular, $L_{x}(y) = xy$ and $R_{x}(y) = yx$ are the left and the right multiplications, and $\Theta_{x}(y) = xyx^{*}$ is the sandwich.

## The Left and the Right Multiplications

**Proposition.** For every $x \in A$,

$$
L_{x}^{*} = L_{x^{*}}, \qquad R_{x}^{*} = R_{x^{t}} .
$$

**Proof.** $h(L_{x}y, z) = h(xy, z) = h(y, x^{*}z) = h(y, L_{x^{*}}z)$ by the compatibility, which is the defining relation of the adjoint; the uniqueness of the adjoint for a nonsingular form identifies $L_{x}^{*}$ with $L_{x^{*}}$. For the right multiplication the element $x^{t}$ is defined by $h(yx,z) = h(y,zx^{t})$, which exists and is unique when $h$ is nonsingular, so $R_{x^{t}}$ is the adjoint of $R_{x}$ by construction, and in a basis with Gram matrix $G$ it is $x^{t} = Gx^{*}G^{-1}$. The two identities agree, $x^{t} = x^{*}$, exactly when the form satisfies the third identity $h(xy,z) = h(x,zy^{*})$; the identity is not a consequence of the compatibility, and on the $2\times2$ matrices over $\mathbb{Z}[\mathrm{i}]$ the left identity holds on all $4096$ triples of the tested set while the right identity by $x^{*}$ holds on all of them for the trace form and fails on $1728$ of them for the compatible form $\tau(xGy^{*})$, $G = \operatorname{diag}(1,-1)$.

**Corollary (the regular representations).** The maps $x \mapsto L_{x}$ and $x \mapsto R_{x}$ are injective on a unital $A$; the first is an algebra homomorphism and a $*$-map, and the second is an algebra anti-homomorphism and a $*$-map, in the sense that it reverses the product while preserving the involution.

**Proof.** Injectivity: $L_{x} = 0$ gives $x = L_{x}1 = 0$, and likewise on the right. Multiplicativity: $L_{xy} = L_{x}L_{y}$ and $R_{xy} = R_{y}R_{x}$ by associativity, and the adjoint identity of the left multiplications is the compatibility with the involution.

## The Sandwich

**Definition.** The **sandwich** of $x$ is the operator $\Theta_{x} : A \to A$, $\Theta_{x}(y) = xyx^{*}$; it is the composite $\Theta_{x} = L_{x} \circ R_{x^{*}} = R_{x^{*}} \circ L_{x}$ of the two one-sided multiplications.

**Proposition.** For every $x \in A$,

$$
\Theta_{x}^{*} = \Theta_{x^{*}} ,
$$

the adjoint of the sandwich by $x$ being the sandwich by $x^{*}$, for a **cyclic** functional $\varphi = h(\cdot,1)$, in particular for the trace form; when $x$ is self-adjoint the sandwich is a self-adjoint operator in the sense of *Self-Adjoint and Skew Operators of a Form*.

**Proof.** $h(xyx^{*}, z) = \varphi(z^{*}xyx^{*}) = \varphi(x^{*}z^{*}xy) = \varphi((x^{*}zx)^{*}y) = h(y, x^{*}zx) = h(y, \Theta_{x^{*}}(z))$, by the identification $h(u,w) = \varphi(w^{*}u)$ of *Sesqualgebras with a Form* and the cyclicity of the functional $\varphi = h(\cdot,1)$: the identity is a statement about the trace form, and it is verified there on the $4096$ triples of the tested set with no failure, while the compatible form $\tau(xGy^{*})$, $G = \operatorname{diag}(1,-1)$, fails it on $1296$ of them.

**Corollary.** The sandwich is a self-adjoint operator exactly when $\Theta_{x} = \Theta_{x^{*}}$, equivalently when $x$ is self-adjoint and commutes with $x^{*}$ in the required sense; on the unitary slice the sandwich is the inner automorphism, $\Theta_{u}(y) = uyu^{-1}$.

## The Unitary Slice and the Inner Automorphism

**Proposition.** Let $u$ be unitary, $u^{*}u = uu^{*} = 1$. Then the sandwich $\Theta_{u}$ is the inner automorphism $y \mapsto uyu^{-1}$, and it is a unitary operator with adjoint $\Theta_{u^{*}} = \Theta_{u}^{-1}$.

**Proof.** On the slice $u^{*} = u^{-1}$, so $\Theta_{u}(y) = uyu^{-1}$ and it is an automorphism of the algebra; as an operator it is the composite of two isometries $L_{u}$ and $R_{u^{-1}} = R_{u^{*}}$, hence an isometry; it is invertible with inverse $\Theta_{u^{-1}}$, and the adjoint identity of the previous section gives $\Theta_{u}^{*} = \Theta_{u^{*}} = \Theta_{u^{-1}} = \Theta_{u}^{-1}$.

**Corollary.** The unitary slice acts on $A$ by algebra automorphisms that are unitary operators; the action is the **inner conjugation** of the two-sided operators, and its infinitesimal version is the derivation $y \mapsto [T,y]$ of the Lie algebra of *The Unitary Group of a Form and Its Lie Algebra*. The general theory of the inner conjugation on the two-sided operators is *The Inner Conjugation on the Two-Sided Operators* and *Hermitian Adjoints on a Hermitian Algebra*.

## The Commutant of the Multiplications

**Proposition.** An operator commutes with every left multiplication exactly when it is a right multiplication; symbolically, $\operatorname{End}_{A}(A) = \{R_{x} : x \in A\}$ when $A$ is unital.

**Proof.** If $T$ is $A$-linear in the sense $T(ax) = aT(x)$ for all $a$, then $T(y) = T(y \cdot 1) = yT(1)$, so $T = R_{T(1)}$; the converse is associativity. The adjoint operation exchanges the two families: the adjoint of an $A$-linear operator is $A$-linear in the opposite-algebra reading, which is the statement $L_{x}^{*} = L_{x^{*}}$ read against $R$.

**Corollary.** The algebra of the left multiplications and the algebra of the right multiplications are mutual commutants, and the adjoint operation exchanges them; the sandwiches commute with the left and the right multiplications of the elements that are central in the required sense.

## What Belongs Elsewhere

- The **conjugate left multiplication** $y \mapsto xy^{*}$ is not a linear operator but a $\varsigma$-semilinear one, and its twisted adjoint is not of the one-sided shape; the computation is *The Adjoint of the One-Sided Action with Hermitian Adjoint* in Part II.
- The **graded and the signed** versions of the same adjoint identities are the signed groups of this category: *Adjoints of the Graded Operators of a Hermitian Algebra* and *The Signed Adjoint of the Sandwich on a Hermitian Algebra*.
- The **bounded** and the **spectral** reading of the same operators, with the adjoint of a multiplication on a complete space, is *The Adjoint of the Left and the Right Multiplication* and *The Adjoint of the Sandwich on a Hermitian Algebra*.
- The **positivity** of $\Theta_{x}$ for positive $x$, and the cone of the sandwich operators, are Part II.

## Examples

### The Matrices

On $M_n(\mathbb{C})$ with the trace form the left multiplication by $X$ has for adjoint the left multiplication by $X^{\dagger}$; the sandwich $\Theta_{X}(Y) = XYX^{\dagger}$ has for adjoint the sandwich by $X^{\dagger}$, and on the unitary group it is the conjugation $Y \mapsto UYU^{-1}$. At $n=2$ the unitary sandwich by $\sigma_1$ and its adjoint are

$$
X=\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}=X^{\dagger},\qquad \Theta_X(\sigma_3)=\sigma_1\sigma_3\sigma_1=-\sigma_3,\qquad \Theta_X^{\dagger}=\Theta_{X^{\dagger}}=\Theta_X .
$$

### The Clifford Algebra

On a Clifford algebra with the dagger, the adjoint of the left multiplication by a vector $v$ is the left multiplication by $v^{\dagger} = -v$ for the signed dagger; the sandwich by a versor is the rotor action of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*, and the two-sided operators of the Clifford category are built from these identities.

### The Biquaternions

On $\mathbb{B}$ with the dagger the sandwich by a biquaternion $\tilde P$ has adjoint the sandwich by $\tilde P^{\dagger}$, and for the unitary slice it is the conjugation of the matrix algebra; the explicit computation is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

## Summary

- The left multiplication has for adjoint the left multiplication by the involution, $L_{x}^{*} = L_{x^{*}}$: this is the compatibility in operator form. The right multiplication obeys $R_{x}^{*} = R_{x^{t}}$ for the transpose of $x$, and the plain identity $R_{x}^{*} = R_{x^{*}}$ is the third identity, which holds for the trace form and not in general.
- The **sandwich** $\Theta_{x}(y) = xyx^{*}$ satisfies $\Theta_{x}^{*} = \Theta_{x^{*}}$ and is the composite of the two one-sided multiplications.
- On the unitary slice the sandwich is the inner automorphism $y \mapsto uyu^{-1}$, a unitary operator with adjoint its inverse.
- The regular representations are injective, the left one a homomorphism and the right one an anti-homomorphism, both compatible with the involution.
- The left multiplications and the right multiplications are mutual commutants, and the adjoint operation exchanges them.
- The conjugate multiplication is semilinear and its adjoint is a Part II object; the graded, signed, bounded and spectral versions of the same identities are the articles named above.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{x}(y) = xy$ | the left multiplication by $x$ |
| $R_{x}(y) = yx$ | the right multiplication by $x$ |
| $\Theta_{x}(y) = xyx^{*}$ | the sandwich of $x$ |
| $T^{*}$ | the adjoint of $T$ for $h$ |
| $\operatorname{End}_{A}(A)$ | the $A$-linear endomorphisms, equal to the right multiplications |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the adjoint of a multiplication and the structure of the algebra of operators.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the multiplications of an algebra with an involution and their adjoints.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. I (Academic Press, 1983), for the completed version of the same identities on a Hilbert space.
