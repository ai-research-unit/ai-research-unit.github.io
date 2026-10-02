
# __The Signed Adjoint Sandwich on a Topological Vector Space__

## Introduction

The trace form of the category is invariant under the grade involution, $\langle\alpha(x), z\rangle = \langle x, \alpha(z)\rangle$, and that invariance computes the adjoint of every signed sandwich on a topological algebra: the adjoint of $\Theta^{\alpha}_{a,b}$ is the signed sandwich $\Theta^{\alpha}_{\alpha(b),\alpha(a)}$, obtained by applying the grade involution to both parameters and exchanging them. The adjoint of the signed left multiplication, which is the case $b = 1$, is therefore the signed right multiplication $\Theta^{\alpha}_{1,\alpha(a)}$, the unsigned case being the familiar adjointness of the left and right multiplications. The list includes a **unitarity criterion:** the two products of a signed sandwich with its adjoint are the unsigned inner sandwiches $\Phi_{u,u}$ and $\Phi_{w,w}$ of the parameters $u = \alpha(b)\alpha(a)$ and $w = ab$, so the sandwich is unitary exactly when those parameters are central involutions, which is the signed form of the element condition $u^{*}u = uu^{*} = 1$.

This article develops the adjoint of the signed sandwich for the trace form. The signed sandwich and its composition law are *The Signed Sandwich on a Topological Vector Space*; the trace form and the adjoint of the unsigned sandwich are *The Adjoint of the Left Multiplication on a Topological Vector Space*; the module-level variant is *The Graded Adjoint Action on a Module over a Topological Vector Space*; the reflection case is *The Signed Adjoint of the Reflection on a Topological Vector Space*. The forms are Part III.

Throughout, $E$ is a Hausdorff locally convex algebra over $\mathbb{K}$ with a unit and jointly continuous multiplication, $\tau$ is a continuous trace and $\langle x, y\rangle = \tau(xy)$ the trace form of the category, assumed non-degenerate, $\alpha$ is a continuous involutive algebra automorphism preserving the trace, $\Phi_{a,b}(x) = axb$ is the unsigned sandwich, $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ is the signed sandwich, and ${}^{\dagger}$ is the trace-adjoint. The grade invariance used throughout is

$$
\langle \alpha(x), z\rangle = \langle x, \alpha(z)\rangle ,
$$

which holds by *The Adjoint of the Left Multiplication on a Topological Vector Space* because $\alpha$ is a trace-preserving involution.

## The Adjoint of the Signed Sandwich

**Theorem (the adjoint computation).** For all $a, b \in E$ the signed sandwich has the trace-adjoint

$$
(\Theta^{\alpha}_{a,b})^{\dagger} = \Theta^{\alpha}_{\alpha(b),\alpha(a)} ,
$$

obtained from $\Theta^{\alpha}_{a,b}$ by applying the grade involution to both parameters and exchanging them; in particular the adjoint of a signed sandwich is again a signed sandwich, and the assignment is an involution of the signed family.

**Proof.** For $x, y \in E$, $\langle \Theta^{\alpha}_{a,b}x, y\rangle = \langle a\alpha(x)b, y\rangle = \tau(a\alpha(x)by) = \tau(\alpha(x)\,bya)$ by the cyclicity of the trace; by the grade invariance this is $\tau(x\,\alpha(bya)) = \tau(x\,\alpha(b)\alpha(y)\alpha(a)) = \langle x, \Theta^{\alpha}_{\alpha(b),\alpha(a)}y\rangle$. Uniqueness of the adjoint in the non-degenerate trace form gives the identity, and applying it twice returns $\Theta^{\alpha}_{a,b}$ because $\alpha^{2} = \mathrm{id}$.

**Corollary (the adjoint of the signed left multiplication).** The signed left multiplication $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1}$ has the adjoint

$$
(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha ,
$$

the signed right multiplication by $\alpha(a)$, mapping $x$ to $\alpha(x)\alpha(a)$; the adjoint of the one-sided signed operator is one-sided, with the parameter imaged by the grade involution and the side exchanged.

**Proof.** This is the theorem with $b = 1$, using $\alpha(1) = 1$ and the identification $\Theta^{\alpha}_{1,\alpha(a)}(x) = \alpha(x)\alpha(a)$.

**Corollary (the unsigned case).** When $\alpha = \mathrm{id}$ the signed sandwich is the unsigned sandwich and the adjoint computation reduces to

$$
(\Phi_{a,b})^{\dagger} = \Phi_{b,a} ,
$$

in agreement with *The Adjoint of the Left Multiplication on a Topological Vector Space*; the signed case therefore specialises to the unsigned one, and the sign enters only through the two applications of $\alpha$ to the parameters.

**Proof.** Set $\alpha = \mathrm{id}$ in the theorem.

## The Unitarity Criterion

**Theorem (the products with the adjoint).** For all $a, b \in E$ the two products of the signed sandwich with its adjoint are the unsigned inner sandwiches

$$
(\Theta^{\alpha}_{a,b})^{\dagger}\,\Theta^{\alpha}_{a,b} = \Phi_{u,u}, \qquad
\Theta^{\alpha}_{a,b}\,(\Theta^{\alpha}_{a,b})^{\dagger} = \Phi_{w,w} ,
$$

with the parameters

$$
u = \alpha(b)\alpha(a) , \qquad w = ab .
$$

**Proof.** For the first, $(\Theta^{\alpha}_{a,b})^{\dagger}\Theta^{\alpha}_{a,b}(x) = \Theta^{\alpha}_{\alpha(b),\alpha(a)}(a\alpha(x)b) = \alpha(b)\,\alpha(a\alpha(x)b)\,\alpha(a) = \alpha(b)\alpha(a)\,x\,\alpha(b)\alpha(a) = uxu$, using $\alpha^{2} = \mathrm{id}$. The second is the same computation with the order of the two factors exchanged, or the first applied to the pair $(b,a)$ read in the reversed algebra; it gives $wxw = abxb a$ with $w = ab$.

**Corollary (the unitarity criterion).** The signed sandwich $\Theta^{\alpha}_{a,b}$ is unitary for the trace form,

$$
(\Theta^{\alpha}_{a,b})^{\dagger}\Theta^{\alpha}_{a,b} = \Theta^{\alpha}_{a,b}(\Theta^{\alpha}_{a,b})^{\dagger} = \mathrm{id} ,
$$

exactly when the parameters $u = \alpha(b)\alpha(a)$ and $w = ab$ are central involutions of $E$; equivalently, when $\Phi_{u,u} = \Phi_{w,w} = \mathrm{id}$, that is when $u, w \in Z(E)$ and $u^{2} = w^{2} = 1$. In particular a signed sandwich with $u$ a central involution and $a, b$ commuting is unitary.

**Proof.** $\Phi_{c,c} = \mathrm{id}$ means $cxc = x$ for all $x$, that is $c \in Z(E)$ and $c^{2} = 1$; applying this to the two products of the theorem gives the criterion, and the sufficient condition follows because $ab = ba$ makes $\alpha(b)\alpha(a) = \alpha(ab)$ central together with $ab$ when the latter is.

**Corollary (the unitarity of the signed left multiplication).** The signed left multiplication $\Lambda^{\alpha}_{a}$ is unitary exactly when $a$ is such that $\alpha(a)$ and $a$ are central involutions; in the unsigned case $\Lambda^{\mathrm{id}}_{a} = L_{a}$ is unitary exactly when $a$ is a central involution, the operator-theoretic form of the element condition $a^{2} = 1$, $a \in Z(E)$.

**Proof.** Apply the criterion with $b = 1$: $u = \alpha(a)$ and $w = a$.

## Examples

**Example (the inner sandwich of an involution).** If $r$ is an involution, $\alpha = \alpha_{r}$ the inner grade involution and $\Theta^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}$ is the inner sandwich of $r$, then its adjoint is $\Theta^{\alpha_{r}}_{\alpha_{r}(r^{-1}),\alpha_{r}(r)} = \Theta^{\alpha_{r}}_{r^{-1},r}$, which is again the identity sandwich, so the inner sandwich is self-adjoint and unitary; its parameters satisfy $u = \alpha_{r}(r^{-1})\alpha_{r}(r) = r^{-1}r = 1$, a central involution, in agreement with the criterion.

**Example (the signed sandwich of a homogeneous pair).** In a graded algebra with the grade involution and $a, b$ homogeneous and invertible, the parameters are $u = \alpha(b)\alpha(a) = (-1)^{p+q}ba$ and $w = ab$; the sandwich is unitary exactly when both are central involutions, which for central $a, b$ reduces to the single sign condition $(-1)^{p+q}(ab)^{2} = 1$.

**Example (the finite-dimensional instance).** For $E = \mathrm{End}_F(V)$ with $\operatorname{tr}$ the criterion becomes that the signed sandwich is unitary exactly when $\alpha(b)\alpha(a)$ and $ab$ are central involutions of the matrix algebra, that is scalar signs; the unitary group it defines is the group of signed sandwiches with central-involution parameters.

## Summary

For the trace form of the category the grade invariance $\langle\alpha(x),z\rangle = \langle x,\alpha(z)\rangle$ computes the adjoint of the signed sandwich, $(\Theta^{\alpha}_{a,b})^{\dagger} = \Theta^{\alpha}_{\alpha(b),\alpha(a)}$, so the adjoint of a signed sandwich is the signed sandwich with the parameters imaged by the grade involution and exchanged; the unsigned case is $(\Phi_{a,b})^{\dagger} = \Phi_{b,a}$ and the signed left multiplication has adjoint $\Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha$. The products of a signed sandwich with its adjoint are the unsigned inner sandwiches $\Phi_{u,u}$ and $\Phi_{w,w}$ of $u = \alpha(b)\alpha(a)$ and $w = ab$, so the sandwich is unitary exactly when those parameters are central involutions, the signed form of $u^{*}u = uu^{*} = 1$; in particular the signed left multiplication is unitary exactly when $\alpha(a)$ and $a$ are central involutions. The inner sandwich of an involution is the basic self-adjoint unitary example. The reflection case is *The Signed Adjoint of the Reflection on a Topological Vector Space*, and the module-level variant is *The Graded Adjoint Action on a Module over a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $\tau$, $\langle x,y\rangle = \tau(xy)$ | the algebra, the trace and the trace form |
| $\alpha$ | trace-preserving grade involution |
| $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ | signed sandwich |
| $(\Theta^{\alpha}_{a,b})^{\dagger} = \Theta^{\alpha}_{\alpha(b),\alpha(a)}$ | the adjoint |
| $(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha$ | the signed left multiplication |
| $(\Theta^{\alpha}_{a,b})^{\dagger}\Theta^{\alpha}_{a,b} = \Phi_{u,u}$ | $u = \alpha(b)\alpha(a)$ |
| $\Theta^{\alpha}_{a,b}(\Theta^{\alpha}_{a,b})^{\dagger} = \Phi_{w,w}$ | $w = ab$ |
| $u, w$ central involutions | the unitarity criterion |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the involutions, the traces and the adjointable operators.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the trace forms and the unitary elements of an operator algebra.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the graded algebras, the grade involution and the sandwiches.
- Gottfried Köthe, *Topological Vector Spaces II* (Springer, 1979), for the topological algebras and their pairings.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological algebras and the bilinear forms.
