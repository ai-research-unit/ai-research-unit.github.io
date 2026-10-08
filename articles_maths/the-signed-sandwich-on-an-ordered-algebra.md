
# __The Signed Sandwich on an Ordered Algebra__

## Introduction

The **unsigned sandwich** of an algebra is the two-parameter operator

$$
\Theta_{a,b} : x\mapsto axb ,
$$

the composition of a left multiplication and a right multiplication, which for $b = a^{-1}$ is an inner automorphism and for $a = b$ is a square. The **signed sandwich** twists the argument by the **grade involution** $\alpha$ of a graded algebra:

$$
\Theta^{\alpha}_{a,b} : x\mapsto a\,\alpha(x)\,b .
$$

The two are related by the grading: if $\Gamma$ is the operator that is $+1$ on the even part and $-1$ on the odd part, then $\Theta^{\alpha}_{a,b} = \Theta_{a,b}\circ\Gamma$, and when the grade involution is inner, $\alpha(x) = uxu^{-1}$, the signed sandwich is an unsigned sandwich with shifted parameters, $\Theta^{\alpha}_{a,b} = \Theta_{au,\,u^{-1}b}$. The signed sandwich therefore adds no new operator in those cases; what it adds is the **twist of the parity**, and its use is the study of the elements on which the twisted conjugation is an involution.

An element $a$ with $\alpha(a) = a^{-1}$ makes the **signed conjugation**

$$
x\mapsto a\,\alpha(x)\,a^{-1}
$$

an operator of order two, that is, a **reflection**. This is the phenomenon the article isolates; the correspondence between the reflections of the algebra and the elements that realise them is the subject of *Reflections as Signed Two-Sided Operators on an Ordered Algebra*, which follows. The article also states when the signed sandwich is **positive**, which is exactly when the grade involution preserves the cone and the parameters are positive.

The ordered algebra, the left and right multiplications and their positivity are *The Left and Right Multiplication Operators on an Ordered Algebra*; the grading, the grade involution and the sign rule are *Superalgebras and Graded Structures* of Part I; the operator order is *Positive Operators on an Ordered Space*; and the involution of the corpus, which is an anti-automorphism and not the grade involution, is *Ordered Involutive Algebras* later in this category. The signed **Hermitian** sandwich $\Theta^{\alpha}_x(y) = \alpha(x)\,y\,x^{\dagger}$ of *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint* of Part II carries the grade involution on the **parameter**; the present article carries it on the **argument**, and the two conventions are different objects with the same name, which is stated in a remark and reconciled in the companion file. The adjoint of the signed sandwich is *The Signed Adjoint Sandwich on an Ordered Algebra* at the end of this category.

## The Grade Involution and the Grading

**Definition.** A **grade involution** of an algebra $A$ is an algebra automorphism $\alpha$ with $\alpha^2 = \mathrm{id}$. It is **inner** when $\alpha(x) = uxu^{-1}$ for a unit $u$, and **positive** when it preserves the cone, $\alpha(A_+)\subseteq A_+$.

**Proposition (the grading).** A grade involution decomposes $A$ as

$$
A = A_{\bar 0}\oplus A_{\bar 1}, \qquad A_{\bar 0} = \ker(\alpha - \mathrm{id}), \quad A_{\bar 1} = \ker(\alpha + \mathrm{id}) ,
$$

the **even** and **odd** parts, when $2$ is invertible in the scalars; $A_{\bar 0}$ is a subalgebra, $A_{\bar 0}A_{\bar 1}\cup A_{\bar 1}A_{\bar 0}\subseteq A_{\bar 1}$, and $A_{\bar 1}A_{\bar 1}\subseteq A_{\bar 0}$. A homogeneous element $x$ has a **parity** $\lvert x\rvert\in\{0,1\}$ with $\alpha(x) = (-1)^{\lvert x\rvert}x$, and the parity is additive, $\lvert xy\rvert = \lvert x\rvert+\lvert y\rvert$ modulo two.

*Proof.* The decomposition is the standard one for an involution with the two eigenvalues $\pm1$; the containment of the products is the multiplicativity of $\alpha$ applied to the eigenvalue equations, since $\alpha(xy) = \alpha(x)\alpha(y)$ multiplies the signs; the parity statement is the definition.

**Proposition (the grading operator).** The **grading operator** $\Gamma$ defined by $\Gamma x = (-1)^{\lvert x\rvert}x$ on the homogeneous elements is linear, satisfies $\Gamma^2 = \mathrm{id}$, and is the diagonalisable operator whose eigenspaces are the even and odd parts; it is an involution of the vector space, not of the algebra, and it equals $\alpha$ as a map of the underlying vector space.

*Proof.* Linearity on the homogeneous pieces and the extension by linearity give the first two claims; the identification with $\alpha$ is the parity formula.

## The Signed Sandwich

### Definition and Linearity

**Definition.** For $a,b\in A$ the **signed sandwich** is the operator

$$
\Theta^{\alpha}_{a,b} : A\to A, \qquad \Theta^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

When $\alpha = \mathrm{id}$ it is the **unsigned sandwich** $\Theta_{a,b}(x) = axb$.

**Proposition.** $\Theta^{\alpha}_{a,b}$ is linear in $x$ and in each parameter; it is $\Theta_{a,b}\circ\Gamma = \Gamma_{l}\circ\Theta_{a,b}$ for the grading operator $\Gamma$ on the argument, so it factors through the unsigned sandwich; and

$$
\Theta^{\alpha}_{a,b} = 0 \iff a = 0 \ \text{or}\ b = 0
$$

in a unital algebra.

*Proof.* Linearity in the parameters is the bilinearity of the multiplication and the linearity of $\alpha$. The factorisation is $\alpha = \Gamma$ on the underlying vector space. The vanishing statement uses $\Theta^\alpha_{a,b}(1) = ab$ in a unital algebra, so $a = 0$ or $b = 0$.

### Composition and the Parameter Law

**Theorem (the composition law).** The signed sandwiches compose by the twisted parameter rule

$$
\Theta^{\alpha}_{a,b}\,\Theta^{\alpha}_{c,d} = \Theta^{\alpha}_{a\,\alpha(c),\,\alpha(d)\,b} ,
$$

which for $\alpha = \mathrm{id}$ is the unsigned law $\Theta_{a,b}\Theta_{c,d} = \Theta_{ac,\,db}$.

*Proof.* Compute $\Theta^{\alpha}_{a,b}\bigl(\Theta^{\alpha}_{c,d}(x)\bigr) = a\,\alpha\bigl(c\,\alpha(x)\,d\bigr)b = a\,\alpha(c)\,\alpha^2(x)\,\alpha(d)\,b = a\alpha(c)\,x\,\alpha(d)\,b$, using that $\alpha$ is an algebra homomorphism and $\alpha^2 = \mathrm{id}$; the result is $\Theta^{\alpha}_{a\alpha(c),\,\alpha(d)b}(x)$.

**Corollary (the parameter algebra).** With the composition as the product the signed sandwiches form a semigroup isomorphic to $A\times A$ with the twisted multiplication $(a,b)(c,d) = (a\alpha(c),\alpha(d)b)$; when $\alpha$ is inner, $\alpha(x) = uxu^{-1}$, the same law is the ordinary multiplication after the shift $(a,b)\mapsto(au,u^{-1}b)$, and the signed sandwiches are the unsigned sandwiches of the shifted pairs.

*Proof.* The semigroup statement is the composition law. For the inner case, $a\alpha(c) = au c u^{-1}$ and $\alpha(d)b = u d u^{-1}b$, so $\Theta^\alpha_{a,b} = \Theta_{au,\,u^{-1}b}$ and the twisted law becomes the ordinary one.

### Positivity

**Proposition (positivity of the signed sandwich).** If the grade involution is **positive** and $a\geq0$, $b\geq0$, then $\Theta^{\alpha}_{a,b}\geq0$. If the grade involution is not positive the signed sandwich of positive parameters need not be positive, and the obstruction is exactly the sign of $\alpha$ on the odd part of the cone; in the graded case with the parity $\varepsilon$, the signed sandwich acts as

$$
\Theta^{\alpha}_{a,b}(x) = \varepsilon_x\,\Theta_{a,b}(x) \quad (x \ \text{homogeneous}) ,
$$

so on the odd part it is the negative of the unsigned sandwich.

*Proof.* Positivity of $\alpha$ gives $\alpha(x)\geq0$ for $x\geq0$, and the product of two positive elements with a positive middle is positive by the positive bilinearity of the ordered algebra. For the parity formula, $\alpha(x) = \varepsilon_x x$, which is the second display; on the odd part $\varepsilon_x = -1$, and the unsigned sandwich of positive parameters is positive while the signed one is negative.

## The Reflections the Sandwich Realises

**Definition.** An element $a\in A$ is a **reflection element** when it satisfies

$$
\alpha(a) = a^{-1} ,
$$

that is, when the grade involution inverts it; it is **normalised** when in addition $a^2 = 1$, and **skew** when $a^2 = -1$.

**Theorem (the signed conjugation is an involution exactly on the reflection elements).** The signed sandwich with $b = a^{-1}$, the **signed conjugation**

$$
\tau_a : x\mapsto a\,\alpha(x)\,a^{-1} ,
$$

is an involution, $\tau_a^2 = \mathrm{id}$, if and only if $\alpha(a) = a^{-1}$. When $\alpha = \mathrm{id}$ the same operator is the ordinary inner conjugation $\tau_a(x) = axa^{-1}$, an automorphism of the algebra for every invertible $a$, and it is an involution if and only if $a^2$ is central.

*Proof.* By the composition law, $\tau_a^2 = \Theta^{\alpha}_{a\alpha(a),\,a^{-1}\alpha(a)^{-1}}$, which is the identity exactly when $a\alpha(a) = 1$ and its inverse, that is, $\alpha(a) = a^{-1}$. In the unsigned case $\tau_a = \Theta_{a,a^{-1}}$ is the conjugation by $a$, and $\tau_a^2 = \Theta_{a^2,\,a^{-2}}$ is the identity exactly when $a^2$ is central.

**Corollary (the odd reflections).** In a graded algebra whose odd part generates, an odd element $a$ with $a^2 = -1$ is a skew reflection element: $\alpha(a) = -a = a^{-1}$, so the signed conjugation $\tau_a(x) = a\alpha(x)a^{-1}$ is an involution, and it acts as the ordinary conjugation on the even part and as its negative on the odd part, $\tau_a = \Theta_{a,a^{-1}}\circ\Gamma$. A normalised even element $a$ with $a^2 = 1$ is a reflection element with $\alpha(a) = a = a^{-1}$, and it acts by the ordinary conjugation.

*Proof.* For odd $a$ with $a^2 = -1$ the inverse is $a^{-1} = -a = \alpha(a)$, so the involution condition holds, and the parity formula of the positivity proposition gives the two cases. For even $a$ with $a^2 = 1$ the inverse is $a = \alpha(a)$ and the signed conjugation is the ordinary one.

**Remark (the boundary of the correspondence).** The theorem gives a reflection operator for every reflection element, but the converse is delicate: an involutive signed sandwich $\Theta^{\alpha}_{a,b}$ with $b\neq a^{-1}$ need not come from a reflection element, and in characteristic two every element is even and the involution condition collapses; the correspondence is therefore a statement about the elements and not about all involutive signed sandwiches, and it is the subject of the next article.

## Worked Cases

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with the grade involution $\alpha$ the conjugation by $\operatorname{diag}(1,-1)$, the parity grading of the biquaternions. The even part is the span of $\operatorname{diag}(1,-1)$ and the identity, the odd part is the span of the off-diagonal matrix units, and an odd $a$ with $a^2 = -1$, such as an off-diagonal matrix unit with a suitable sign, realises the signed conjugation as an involution of order two. The signed sandwich $\Theta^{\alpha}_{a,b}$ with general parameters is an unsigned sandwich after the inner shift, since $\alpha$ is inner in $M_2(\mathbb{C})$; this is the model in which the signed and the unsigned sandwiches are the same operator family under a shift of the parameters, and it shows that the interest of the signed sandwich lies in the **fixed parameters**, not in the operator family.

### The Group Algebra

Let $A = \mathbb{R}[G]$ for a group $G$ with a homomorphism $\lvert\cdot\rvert : G\to\mathbb{Z}/2$ to the parity group, extended to the grade involution $\alpha(g) = (-1)^{\lvert g\rvert}g$. An **even** involution $g$ with $\lvert g\rvert = 0$ and $g^2 = 1$ is a reflection element, since $\alpha(g) = g = g^{-1}$, and the signed conjugation is the ordinary conjugation by $g$. An **odd** element with $g^2 = -1$ is a skew reflection element, since then $g^{-1} = -g = \alpha(g)$; in the group algebra of the quaternion group such an element exists and the signed conjugation is an involution. An odd element of order two is never a reflection element in characteristic zero, because $\alpha(g) = -g$ while $g^{-1} = g$ and $2g\neq0$. This is the group-theoretic instance of the two classes of reflection elements.

### The Self-Adjoint Matrices

Let $A = H_n(\mathbb{R})$ as the ordered algebra of *Jordan Algebras and the Positive Cone*, with the grade involution the identity and the order the Loewner one. The signed sandwich is then the ordinary sandwich $\Theta_{a,b}(x) = axb$ of the symmetrised product, the reflection elements are the involutions $a = a^{-1}$, and the signed conjugation is the ordinary conjugation by an involution. The positivity of the sandwich is not automatic in the associative matrix algebra — the product of positive matrices is not symmetrised-positive — which is why the ordered matrix algebra is the Jordan structure and not the associative one.

## Summary

A **grade involution** is an algebra automorphism $\alpha$ of order two; it decomposes the algebra into the **even** and **odd** parts, it is **inner** when it is a conjugation and **positive** when it preserves the cone, and the grading operator $\Gamma$ realises it on the underlying vector space. The **signed sandwich** $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ is linear, it factors as the unsigned sandwich $\Theta_{a,b}(x) = axb$ composed with $\Gamma$, it is an unsigned sandwich with shifted parameters when $\alpha$ is inner, and it composes by the twisted law $\Theta^\alpha_{a,b}\Theta^\alpha_{c,d} = \Theta^\alpha_{a\alpha(c),\,\alpha(d)b}$. It is **positive** exactly when the grade involution preserves the cone; in the graded case it is the unsigned sandwich on the even part and its negative on the odd part, $\Theta^\alpha_{a,b}(x) = \varepsilon_x\Theta_{a,b}(x)$. The **signed conjugation** $x\mapsto a\alpha(x)a^{-1}$ is an **involution exactly on the reflection elements** $\alpha(a) = a^{-1}$; odd skew elements with $a^2 = -1$ and even normalised elements with $a^2 = 1$ are the two classes, and the correspondence between the reflections and the elements that realise them is the subject of the next article. The unsigned sandwich and the one-sided multiplications are *The Left and Right Multiplication Operators on an Ordered Algebra*; the grading and the grade involution are *Superalgebras and Graded Structures*; the positivity is *Positive Operators on an Ordered Space*; the involution of the corpus is *Ordered Involutive Algebras*; the Hermitian signed sandwich of Part II is *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*; and the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | Grade involution, an algebra automorphism of order two |
| $A_{\bar 0}, A_{\bar 1}$ | Even and odd parts of the graded algebra |
| $\lvert x\rvert$, $\varepsilon_x = (-1)^{\lvert x\rvert}$ | Parity and its sign |
| $\Gamma$ | Grading operator, $\Gamma x = (-1)^{\lvert x\rvert}x$ |
| $\Theta_{a,b}(x) = axb$ | Unsigned sandwich |
| $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $\Theta^\alpha_{a,b}\Theta^\alpha_{c,d} = \Theta^\alpha_{a\alpha(c),\,\alpha(d)b}$ | Composition law |
| $\tau_a(x) = a\alpha(x)a^{-1}$ | Signed conjugation |
| $\alpha(a) = a^{-1}$ | Reflection element, making $\tau_a$ an involution |

## Further Reading

- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the grade involution and the parity of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the graded structure, the sign rule and the reflections realised by conjugation.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the inner automorphisms and the double centralizers of an operator algebra.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the sandwich operators of a Jordan structure and the symmetrised product.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for the automorphisms and the conjugations of an associative algebra.
