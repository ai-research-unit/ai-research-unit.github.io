# __The Signed Adjoint Sandwich on a Jordan Algebra__

## Introduction

The two-sided operators of a special Jordan algebra $J = A^+$ are the sandwich $S_{a,b}(x) = axb$ of the ambient associative algebra and its symmetrisation, the **quadratic representation** $U_{a,b} = \tfrac12(U_{a+b}-U_a-U_b)$; when the ambient algebra carries a **grade involution** $\alpha$, the sandwich admits the **signed** version $S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b$, whose symmetrisation is

$$
\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha ,
$$

the signed sandwich of *The Signed Sandwich on a Jordan Algebra*. The **natural pairing** of the category is the trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$ of *The Adjoint of the Left Multiplication on a Jordan Algebra*, and the present article computes the adjoint of the signed sandwich with respect to it. Because the trace form is **associative**, $T(x\circ y,z) = T(x,y\circ z)$, every left multiplication is self-adjoint, $L_a^{\dagger} = L_a$; because the grade involution is an **isometry**, $T(\alpha x,\alpha y) = T(x,y)$, the involution itself is self-adjoint, $\alpha^{\dagger} = \alpha$; and because the quadratic representation is a polynomial in the self-adjoint left multiplications, it is self-adjoint, $U_{a,b}^{\dagger} = U_{a,b}$. Together these give the explicit expression

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{\dagger} = U_{\alpha(a),\alpha(b)}\circ\alpha = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} ,
$$

the adjoint of the signed sandwich is the signed sandwich at the images of its parameters. The signed sandwich is **unitary** when $U_{a,b}$ is an involution, $U_{a,b}^2 = \mathrm{id}$, the Jordan form of the condition $u^{*}u = uu^{*} = 1$.

After the definitions the article proves the $\alpha$-invariance of the trace form, computes the adjoint of the quadratic representation and then of the signed sandwich, specialises to the diagonal signed sandwich $S^{\alpha}_{u,u^{-1}}$ and to the symmetrisation at a symmetry, and states the **unitarity condition** $U_{a,b}^2 = \mathrm{id}$. The article assumes *The Signed Sandwich on a Jordan Algebra* for the signed sandwich, its symmetrisation and the diagonal case; *The Adjoint of the Left Multiplication on a Jordan Algebra* for the trace form, its associativity and the self-adjointness of $L_a$ and $U_a$; *The Left and Right Multiplication Operators on a Jordan Algebra* for the quadratic representation and the fundamental formula; *The Adjoint of an Endomorphism* for the adjoint with respect to a pairing; and *Involutive Linear Algebras* for the involution of the endomorphism algebra. Throughout, $J = A^+$ is a special unital Jordan algebra over a commutative ring $R$ in which $2$ is invertible, $\alpha$ is a grade involution of $A$ (an automorphism of order two, hence an automorphism of $J$), $T$ is the trace form, and ${}^{\dagger}$ is its adjoint; no norm, form, distance or geometric reflection occurs. The reflection case is *The Signed Adjoint of the Reflection on a Jordan Algebra*, and the one-sided case is *The Signed Adjoint of the Left Multiplication on a Jordan Algebra*.

## The Natural Pairing and Its Compatibility

### The Trace Form

**Definition.** The **natural pairing** of the category on a finite-dimensional Jordan algebra $J$ is the trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$, the trace of the left multiplication by the Jordan product; the **adjoint** of an operator $F$ on $J$ is the unique $F^{\dagger}$ with $T(Fx,y) = T(x,F^{\dagger}y)$.

**Theorem (associativity).** The trace form is symmetric and associative, $T(x\circ y,z) = T(x,y\circ z)$; it is non-degenerate when $J$ is semisimple, and it is invariant under the left multiplications, $T(L_ax,y) = T(x,L_ay)$, so that

$$
L_a^{\dagger} = L_a .
$$

*Proof.* This is *The Adjoint of the Left Multiplication on a Jordan Algebra*; the associativity is the statement $T(L_ax,z) = T(x,L_az)$, which is exactly the self-adjointness of $L_a$ by the uniqueness of the adjoint. $\square$

### The Grade Involution Is an Isometry

**Theorem.** The grade involution $\alpha$ preserves the trace form,

$$
T(\alpha x,\alpha y) = T(x,y) , \qquad \text{hence} \qquad T(\alpha x,y) = T(x,\alpha y) , \qquad \alpha^{\dagger} = \alpha .
$$

*Proof.* For an automorphism $\varphi$ of $J$ one has $L_{\varphi a} = \varphi L_a\varphi^{-1}$; with $\varphi = \alpha$ and the trace invariant under conjugation, $T(\alpha x,\alpha y) = \operatorname{tr}(L_{\alpha(x\circ y)}) = \operatorname{tr}(\alpha L_{x\circ y}\alpha^{-1}) = \operatorname{tr}(L_{x\circ y}) = T(x,y)$. Replacing $y$ by $\alpha y$ and using $\alpha^2 = \mathrm{id}$ gives $T(\alpha x,y) = T(x,\alpha y)$, which is the defining relation of the adjoint $\alpha^{\dagger} = \alpha$. $\square$

**Corollary (the quadratic representation).** The quadratic representations are self-adjoint, $U_a^{\dagger} = U_a$ and $U_{a,b}^{\dagger} = U_{a,b}$, because they are polynomials in the self-adjoint left multiplications and the symmetrisation preserves self-adjointness.

## The Adjoint of the Signed Sandwich

### The Main Computation

**Theorem.** The adjoint of the symmetrised signed sandwich is the symmetrised signed sandwich at the images of the parameters:

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{\dagger} = \bigl(U_{a,b}\circ\alpha\bigr)^{\dagger} = U_{\alpha(a),\alpha(b)}\circ\alpha = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} .
$$

*Proof.* The adjoint is anti-multiplicative, $(\Phi\circ\Psi)^{\dagger} = \Psi^{\dagger}\circ\Phi^{\dagger}$, so $(U_{a,b}\circ\alpha)^{\dagger} = \alpha^{\dagger}\circ U_{a,b}^{\dagger} = \alpha\circ U_{a,b}$. Since $\alpha$ is an automorphism, $\alpha\,U_{a,b}\,\alpha^{-1} = U_{\alpha(a),\alpha(b)}$, that is $\alpha\,U_{a,b} = U_{\alpha(a),\alpha(b)}\,\alpha$; substituting gives the displayed sandwich. The symmetry $U_{a,b} = U_{b,a}$ of the quadratic representation leaves the parameter order, so only the images under $\alpha$ intervene. $\square$

**Corollary (the special-algebra form).** On a special Jordan algebra the unsigned sandwich $S_{a,b}(x) = axb$ has the unsigned adjoint $S^{\dagger}_{a,b}$ given by the same rule at the images of the parameters when the ambient algebra is commutative, and its symmetrisation $\Sigma^{\alpha}_{a,b}$ has the adjoint $\Sigma^{\alpha}_{\alpha(a),\alpha(b)}$ by the theorem; the adjoint of the signed sandwich is again a signed sandwich.

### The Diagonal Signed Sandwich

**Theorem.** The diagonal signed sandwich $S^{\alpha}_{u,u^{-1}}(x) = u\,\alpha(x)\,u^{-1}$ has as symmetrisation the twisted quadratic representation $U_u\circ\alpha$, whose adjoint is

$$
\bigl(U_u\circ\alpha\bigr)^{\dagger} = U_{\alpha(u)}\circ\alpha .
$$

*Proof.* Apply the theorem with $a = b = u$ and $U_{u,u} = U_u$. $\square$

**Corollary.** The adjoint of the signed conjugation $x\mapsto u\alpha(x)u^{-1}$ is the signed conjugation by $\alpha(u)$; in particular the reflection at a symmetry is self-adjoint exactly when $\alpha(u) = u$, which is the content of *The Signed Adjoint of the Reflection on a Jordan Algebra*.

## Unitarity

**Theorem (the unitarity condition).** The signed sandwich is unitary with respect to the adjoint, $(\Sigma^{\alpha}_{a,b})^{\dagger}\Sigma^{\alpha}_{a,b} = \Sigma^{\alpha}_{a,b}(\Sigma^{\alpha}_{a,b})^{\dagger} = \mathrm{id}$, exactly when the quadratic representation is an involution:

$$
U_{a,b}^2 = \mathrm{id} .
$$

*Proof.* $\Sigma^{\alpha}_{a,b}{}^{\dagger}\Sigma^{\alpha}_{a,b} = U_{\alpha(a),\alpha(b)}\alpha\,U_{a,b}\alpha = U_{\alpha(a),\alpha(b)}U_{\alpha(a),\alpha(b)}\alpha^2 = U_{\alpha(a),\alpha(b)}^2$, and similarly $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{a,b}{}^{\dagger} = U_{a,b}^2$; the two are the identity together exactly when $U_{a,b}^2 = \mathrm{id}$, equivalently $U_{\alpha(a),\alpha(b)}^2 = \mathrm{id}$. $\square$

**Corollary.** The unitarity condition $U_{a,b}^2 = \mathrm{id}$ is the Jordan form of the element condition $u^{*}u = uu^{*} = 1$; for the diagonal sandwich it reads $U_u^2 = \mathrm{id}$, the statement that the twisted quadratic representation is an involution, and it holds for the symmetries.

## Examples

**Example (the identity grade involution).** For $\alpha = \mathrm{id}$ the signed sandwich is the unsigned one $\Sigma^{\alpha}_{a,b} = U_{a,b}$ and the adjoint is $U_{a,b}^{\dagger} = U_{a,b}$, so every unsigned sandwich is self-adjoint; the unitary ones are those with $U_{a,b}^2 = \mathrm{id}$.

**Example (the symmetric matrices).** Let $J = H_n(F)$ with $x\circ y = \tfrac12(xy+yx)$ and the transpose grade involution on the ambient matrix algebra; then $U_a(x) = axa$ and $U_{a,b}(x) = \tfrac12(axb+bxa)$; the signed sandwich $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ has the adjoint $U_{a^{\mathsf{T}},b^{\mathsf{T}}}\circ\alpha$, and it is unitary when $U_{a,b}$ is an involution.

## Summary

The **natural pairing** on a Jordan algebra is the **trace form** $T(x,y) = \operatorname{tr}(L_{x\circ y})$, symmetric, associative and non-degenerate in the semisimple case; its associativity makes every left multiplication self-adjoint, $L_a^{\dagger} = L_a$, and the **grade involution** is an isometry, $T(\alpha x,\alpha y) = T(x,y)$, hence self-adjoint, $\alpha^{\dagger} = \alpha$. The quadratic representations are self-adjoint, $U_{a,b}^{\dagger} = U_{a,b}$, and the adjoint of the **signed sandwich** $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ is the signed sandwich at the images of the parameters,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{\dagger} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} .
$$

The signed sandwich is **unitary** exactly when $U_{a,b}^2 = \mathrm{id}$, the Jordan form of the condition $u^{*}u = uu^{*} = 1$. The diagonal signed sandwich $S^{\alpha}_{u,u^{-1}}$ has the adjoint $U_{\alpha(u)}\circ\alpha$. The identity and the symmetric matrices are the worked examples. No norm, form, distance or geometric reflection occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J = A^+$ | Special unital Jordan algebra |
| $\alpha$ | Grade involution (automorphism of order two) |
| $T(x,y) = \operatorname{tr}(L_{x\circ y})$ | Natural pairing, the trace form |
| $T(x\circ y,z) = T(x,y\circ z)$ | Associativity of the trace form |
| $L_a^{\dagger} = L_a$, $\alpha^{\dagger} = \alpha$ | Self-adjointness of the multiplications and the involution |
| $U_{a,b} = \tfrac12(U_{a+b}-U_a-U_b)$ | Polarised quadratic representation, self-adjoint |
| $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ | Signed sandwich |
| $(\Sigma^{\alpha}_{a,b})^{\dagger} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)}$ | Adjoint of the signed sandwich |
| $U_{a,b}^2 = \mathrm{id}$ | Unitarity condition |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the quadratic representation, the trace form and the symmetries.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the quadratic maps, the sandwiches and their adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the signed sandwiches, the involutions and the unitarity conditions.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the trace form, the quadratic representation and the structure group.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the multiplication algebra, the sandwiches and the pairings.
