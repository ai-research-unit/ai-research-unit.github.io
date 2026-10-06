# __The Continuous Involution and the Spectral Radius__

## Introduction

A complete normed sesquialgebra is read by two maps at once, the product and the involution $*$ of the datum $(R,\varsigma)$, and its norm is a choice made on top of them. This article reads the one condition that ties the three together, the **$\mathrm{C}^{*}$-condition** $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$ of *The Norm Defined by a Form*, §*The $\mathrm{C}^{*}$-Condition*. Under it the norm ceases to be an extra datum: the spectral radius of the self-adjoint element $x^{*}x$, an invariant defined by invertibility alone, computes it,

$$
\lVert x\rVert = r(x^{*}x)^{1/2} = r(xx^{*})^{1/2} = r(x \star x)^{1/2},
$$

and the derived operation $x \star y = xy^{*}$ of the layer is the product in which the identity is read. The article is the sesquialgebra reading of *The Involution and the Spectral Radius*: the same identities, on the general datum $(R,\varsigma)$ rather than on a complex $\mathrm{C}^{*}$-algebra, and with the spectrum moved by the base involution rather than by the conjugation.

Four facts organise the article. **The involution twists the spectrum.** Invertibility is preserved by $*$ in the form $(\lambda - x)^{*} = \varsigma(\lambda) - x^{*}$, so $\sigma(x^{*}) = \varsigma(\sigma(x))$ and $r(x^{*}) = r(x)$; in the sesquilinear kind the spectrum is reflected, $\sigma(x^{*}) = \overline{\sigma(x)}$, and in the bilinear kind it is fixed, $\sigma(x^{*}) = \sigma(x)$. The sesquilinear content of the article is this twist and the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ in which the radius is read. **The radius of the derived square is the norm.** The element $x \star x = xx^{*}$ is self-adjoint and its radius is $\lVert x\rVert^{2}$, so the norm is a formula in the $*$-algebra; the associative square $x^{2}$ does not do the same job, its radius being $r(x)^{2}$ and not $\lVert x\rVert^{2}$, and $0$ for a quasi-nilpotent element of norm one. **The formula forces rigidity.** Because the norm is $r(x \star x)^{1/2}$, the datum $(A,*,R,\varsigma)$ determines it, a $*$-algebra carries at most one $\mathrm{C}^{*}$-norm, unital $*$-homomorphisms are contractive and injective ones isometric. **The radius is not itself a norm.** It is homogeneous, bounded by the norm and multiplicative on the spectrum of a product, $r(xy) = r(yx)$, but it is neither subadditive nor submultiplicative, so it is a norm only in the commutative semisimple case; the $\mathrm{C}^{*}$-norm is the square root of the radius of the *derived* square and not the radius itself.

The article reads the spectrum and the radius on the layer, proves the identity and the positivity of the derived square, proves the twist of the spectrum and the normal cases, states the rigidity and the uniqueness, records the failures of the radius as a norm, and treats the collapse and the examples. The continuity of the involution, the isometric normal form and the $\mathrm{C}^{*}$-case as the free one are *The Continuity of the Involution*, the spectral radius, the radius formula, the $\mathrm{C}^{*}$-identity and the contractivity of the classical complex case are *The Involution and the Spectral Radius*, the reality of the spectrum of a self-adjoint element and the norm formula for it are *The Spectrum of a Self-Adjoint Element*, the positivity and the order that the derived square uses are *Hermitian and Self-Adjoint Elements of a Banach Algebra*, the spectral radius of a Banach algebra is *Topological Algebras and Banach Algebras*, the completion is *The Completion of a Sesquialgebra*, the normed and complete objects are *Banach Sesquialgebras*, and the involutive Banach algebras and the Gelfand–Naimark theorem are *Involutive Banach Algebras and the Gelfand–Naimark Theorem*.

**Conventions.** The datum is $(R,\varsigma)$ with $R = \mathbb{K}$ equal to $\mathbb{R}$ with $\varsigma = \mathrm{id}$ or to $\mathbb{C}$ with $\varsigma$ the conjugation, so that $k = \mathbb{R}$ is the fixed field in both kinds; the **modulus** of a scalar is $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$, the absolute value at $\varsigma = \mathrm{id}$. The algebra $A$ is a **Banach sesquialgebra** over $(R,\varsigma)$: a complete normed $R$-algebra with submultiplicative norm and a continuous $\varsigma$-semilinear involution $*$, $(xy)^{*} = y^{*}x^{*}$, $*^{2} = \mathrm{id}$, $(\lambda x)^{*} = \varsigma(\lambda)x^{*}$; by the normal form of *The Continuity of the Involution*, §*The Normal Form of a Continuous Involution*, the norm may be replaced by $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$, which is equivalent, submultiplicative and invariant under $*$, so the article assumes the involution **isometric**, $\lVert x^{*}\rVert = \lVert x\rVert$. The **derived operation** is $x \star y = xy^{*}$, the **spectrum** is $\sigma(x) = \{\lambda \in \mathbb{C} : \lambda \cdot 1 - x \text{ is not invertible}\}$, read in the complexification $A_{\mathbb{C}} = A \otimes_{\mathbb{R}} \mathbb{C}$ when $R = \mathbb{R}$, so that it is a nonempty compact subset of $\mathbb{C}$ contained in the disk of radius $\lVert x\rVert$ and stable under the conjugation in the real kind; the **spectral radius** is $r(x) = \sup\{\lvert\lambda\rvert : \lambda \in \sigma(x)\}$, finite and attained.

## The Spectrum and the Radius

### The Radius on the Layer

**Proposition (elementary properties).** For all $x, y \in A$ and $\lambda \in R$,

$$
r(x) \leq \lVert x\rVert, \qquad r(\lambda x) = \lvert\lambda\rvert\,r(x), \qquad r(xy) = r(yx), \qquad r(x^{*}) = r(x) .
$$

*Proof.* The first is the standard bound $\lvert\lambda\rvert \leq \lVert x\rVert$ for $\lambda \in \sigma(x)$, from the convergence of the Neumann series $\sum_n x^{n}/\lambda^{n+1}$ for $\lvert\lambda\rvert > \lVert x\rVert$, by *Topological Algebras and Banach Algebras*; the second is $\sigma(\lambda x) = \lambda\sigma(x)$ for a central scalar $\lambda$; the third is $1 - xy$ invertible iff $1 - yx$ invertible with $(1-xy)^{-1} = 1 + x(1-yx)^{-1}y$, which gives $\sigma(xy) \setminus \{0\} = \sigma(yx) \setminus \{0\}$; the last is proved below, and is recorded here for the completeness of the list. $\square$

**Theorem (the radius formula).** The spectral radius is the limit

$$
r(x) = \lim_{n}\lVert x^{n}\rVert^{1/n} = \inf_{n \geq 1}\lVert x^{n}\rVert^{1/n},
$$

and in particular $r(x) = r(y)$ as soon as $\lVert x^{n}\rVert = \lVert y^{n}\rVert$ for all $n$.

*Proof.* The formula is the Gelfand–Beurling formula of *Topological Algebras and Banach Algebras*, §*Banach Algebras*, valid for a complete normed algebra over a valued field; the infimum equals the limit by Fekete's lemma applied to the subadditive sequence $n \mapsto \log\lVert x^{n}\rVert$. $\square$

**Remark (the modulus is the layer's absolute value).** The radius is a nonnegative element of $k$, since $\sigma(x)$ is a set of scalars and $\lvert\varsigma(\lambda)\rvert = \lvert\lambda\rvert$; at $\varsigma = \mathrm{id}$ the modulus is the absolute value of the ordered field and the two readings coincide, and at $\varsigma$ the conjugation the modulus is the usual modulus of $\mathbb{C}$. The squaring $\lvert\lambda\rvert^{2} = \lambda\varsigma(\lambda)$ is the reason the identities below are read with $\varsigma$ in place of the identity.

## The $\mathrm{C}^{*}$-Identity on the Layer

### The Identity and the Derived Square

**Definition.** A Banach sesquialgebra is a **$\mathrm{C}^{*}$-sesquialgebra** when its norm satisfies the **$\mathrm{C}^{*}$-condition**

$$
\lVert x^{*}x\rVert = \lVert x\rVert^{2} \qquad \text{for every } x \in A ,
$$

the axiom stated for the normed object in *The Norm Defined by a Form*, §*The $\mathrm{C}^{*}$-Condition*, and the condition that makes the involution isometric.

**Theorem (the identity).** In a $\mathrm{C}^{*}$-sesquialgebra, for every $x$,

$$
\lVert x^{*}x\rVert = \lVert xx^{*}\rVert = \lVert x \star x\rVert = \lVert x\rVert^{2}, \qquad
\lVert x\rVert = r(x^{*}x)^{1/2} = r(xx^{*})^{1/2} = r(x \star x)^{1/2} .
$$

*Proof.* The element $xx^{*}$ is the star of $x^{*}x$, so $\lVert xx^{*}\rVert = \lVert x^{*}x\rVert$ once the involution is isometric, and the isometry is the theorem of *The Continuity of the Involution*, §*The $\mathrm{C}^{*}$-Condition*, or one line from the condition: $\lVert x\rVert^{2} = \lVert x^{*}x\rVert \leq \lVert x^{*}\rVert\lVert x\rVert$ gives $\lVert x\rVert \leq \lVert x^{*}\rVert$, and $x^{**} = x$ gives the reverse. The element $y = x^{*}x$ is self-adjoint, and for a self-adjoint $y$ the identity $\lVert y^{2}\rVert = \lVert y^{*}y\rVert = \lVert y\rVert^{2}$ iterates to $\lVert y^{2^{n}}\rVert = \lVert y\rVert^{2^{n}}$, so that $r(y) = \lim_{n}\lVert y^{2^{n}}\rVert^{1/2^{n}} = \lVert y\rVert$; hence $\lVert x^{*}x\rVert = r(x^{*}x)$. The radius formula is applied at $x \star x = xx^{*}$. $\square$

**Corollary (the derived square is positive, and computes the norm).** For every $x$ the element $x \star x = xx^{*}$ is self-adjoint with spectrum contained in $[0,\infty)$ and

$$
r(x \star x) = \lVert x \star x\rVert = \lVert x\rVert^{2}, \qquad \lVert x\rVert = r(x \star x)^{1/2} .
$$

*Proof.* The element $x \star x = xx^{*}$ is a product of an element with its star; it is self-adjoint by the involution laws, and its spectrum lies in the nonnegative part of $k$ by the positivity of the $\mathrm{C}^{*}$-algebra, *Hermitian and Self-Adjoint Elements of a Banach Algebra*, §*The Positive Cone and the Order*. Its radius is then its norm by the theorem, and the norm is $\lVert x\rVert^{2}$ by the identity. $\square$

**Remark (the associative square is not the derived one).** The identity of the theorem is a statement about $x \star x$ and not about $x^{2}$. The radius formula read on the even powers gives $r(x^{2}) = \lim_{n}\lVert x^{2n}\rVert^{1/n} = r(x)^{2}$, so $r(x^{2}) = r(x)^{2} \leq \lVert x\rVert^{2}$, the inequality being an equality for the normal elements and strict for the nilpotent below; in no case does the associative square give the norm, whose reading requires the self-adjoint element $x \star x$. For the nilpotent $N$ with $N^{2} = 0$ and $\lVert N\rVert = 1$ the radius of $N$ and of $N^{2}$ is $0$ while the derived square has $r(N \star N) = \lVert N \star N\rVert = 1$. The norm is read from the radius of the derived square, which is self-adjoint, and never from the radius of the associative square, which need not be.

### The Identity Is a Restriction

**Remark (the condition is not automatic).** Submultiplicativity does not imply the $\mathrm{C}^{*}$-condition: on $M_{n}(\mathbb{C})$ with the trace form the Frobenius norm is submultiplicative and at the identity $\lVert 1\rVert^{2} = n$ while $\lVert 1^{*}1\rVert = \sqrt{n}$, so the condition fails for $n \geq 2$; the witness is *The Norm Defined by a Form*, §*The $\mathrm{C}^{*}$-Condition*, and the finite-dimensional model of the failure on the biquaternion algebra is in the examples below. The condition is the hypothesis under which the norm is determined by the spectrum, and it is the only one the identities of this article use beyond completeness and submultiplicativity.

## The Involution and the Spectrum

### The Twist of the Spectrum

**Theorem (the spectrum under the involution).** For every $x \in A$,

$$
\sigma(x^{*}) = \varsigma(\sigma(x)) = \{\varsigma(\lambda) : \lambda \in \sigma(x)\}, \qquad r(x^{*}) = r(x) .
$$

*Proof.* The involution is additive and satisfies $(\lambda \cdot 1 - x)^{*} = \varsigma(\lambda) \cdot 1 - x^{*}$; an element $a$ is invertible iff $a^{*}$ is, with $(a^{*})^{-1} = (a^{-1})^{*}$, because $aa^{-1} = a^{-1}a = 1$ transforms under $*$ into $a^{*}(a^{-1})^{*} = (a^{-1})^{*}a^{*} = 1$. Hence $\varsigma(\lambda) \cdot 1 - x^{*}$ is invertible iff $\lambda \cdot 1 - x$ is, which is the equality of the spectra; the radii agree because $\lvert\varsigma(\lambda)\rvert = \lvert\lambda\rvert$. In the real kind, where the spectrum is read in the complexification and the extended involution carries $\lambda$ to $\bar\lambda$, the same computation gives $\sigma(x^{*}) = \overline{\sigma(x)}$, and this is $\sigma(x)$ itself because the spectrum of an element of a real algebra is stable under the conjugation. $\square$

**Corollary (the two kinds).** In the sesquilinear kind, $R = \mathbb{C}$ with $\varsigma$ the conjugation and

$$
\sigma(x^{*}) = \overline{\sigma(x)} = \{\bar\lambda : \lambda \in \sigma(x)\},
$$

the reflection of the spectrum in the real axis. In the bilinear kind, $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $\sigma(x^{*}) = \sigma(x)$, the involution fixing the spectrum pointwise.

*Proof.* The two readings of the theorem at the two data. $\square$

**Remark (the twist is the sesquilinear content).** The two clauses of the corollary are the layer's form of the classical statement $\sigma(a^{*}) = \overline{\sigma(a)}$ of *The Involution and the Spectral Radius*, and the difference between them is the difference between the two categories: with a nontrivial base involution the involution of the algebra reflects the spectrum, at the collapse it fixes it. The radius is insensitive to the twist, $r(x^{*}) = r(x)$, which is why every statement of the next section holds in both kinds and why they are recorded once.

### Self-Adjoint and Normal Elements

**Theorem (the normal case).** Let $x^{*}x = xx^{*}$. Then

$$
\lVert x\rVert = r(x), \qquad r(x^{*}x) = r(x)^{2}, \qquad \lVert x^{2}\rVert = \lVert x\rVert^{2} .
$$

In particular the statements hold for the self-adjoint elements, $x^{*} = x$.

*Proof.* For a normal $x$ the element $x^{2}$ is normal and $(x^{2})^{*}x^{2} = (x^{*}x)^{2}$, so the $\mathrm{C}^{*}$-condition gives $\lVert x^{2}\rVert^{2} = \lVert (x^{2})^{*}x^{2}\rVert = \lVert (x^{*}x)^{2}\rVert = \lVert x^{*}x\rVert^{2} = \lVert x\rVert^{4}$, that is $\lVert x^{2}\rVert = \lVert x\rVert^{2}$; by induction $\lVert x^{2^{n}}\rVert = \lVert x\rVert^{2^{n}}$ and the radius formula gives $r(x) = \lVert x\rVert$. The second identity is the theorem of the preceding section read at $x^{*}x = xx^{*}$, whose radius is $r(x)^{2}$ by the first. $\square$

**Theorem (the self-adjoint spectrum).** Let $x^{*} = x$. Then $\sigma(x) \subseteq k$ and $r(x) = \lVert x\rVert$; the spectrum is a nonempty compact subset of the fixed field $k$ contained in $[-\lVert x\rVert,\lVert x\rVert]$, and at least one of the two endpoints $\pm\lVert x\rVert$ lies in it.

*Proof.* The reality of the spectrum of a self-adjoint element and the norm formula are *The Spectrum of a Self-Adjoint Element* for the complex kind, and the same two statements over $(\mathbb{R},\mathrm{id})$ for the collapsed kind, whose proof is the real form of the cited one; the containment $\sigma(x) \subseteq k$ is the reality read in the fixed field, and the bound is the elementary $\lvert\lambda\rvert \leq \lVert x\rVert$. The normal case of the preceding theorem contains the norm formula again and is independent of the reality statement. $\square$

**Corollary (the unitary elements).** Let $x^{*}x = xx^{*} = 1$. Then $\lVert x\rVert = 1$, $\sigma(x) \subseteq \{\lambda : \lvert\lambda\rvert = 1\}$ and $r(x) = 1$.

*Proof.* The element is normal, so $\lVert x\rVert = r(x)$ and $\lVert x\rVert^{2} = \lVert x^{*}x\rVert = 1$; the elements of the spectrum are mapped to the unit circle because $\lvert\lambda\rvert \leq \lVert x\rVert = 1$ and $\lvert\lambda^{-1}\rvert \leq \lVert x^{-1}\rVert = \lVert x^{*}\rVert = 1$, both inequalities being the elementary bound. $\square$

**Remark (the fixed field is the home of the spectrum).** In the sesquilinear kind the self-adjoint elements have real spectrum although the scalars are complex, so the fixed field $k$ and not the base is where the spectrum of a self-adjoint element lives; the statement is the layer's form of the reality of the spectrum, and it is what makes the radius of a self-adjoint element a genuine length, $r(x) = \lVert x\rVert$, comparable with the norm.

## The Rigidity of the Norm

### The Formula and the Uniqueness

**Theorem (the norm is a formula in the algebra).** In a $\mathrm{C}^{*}$-sesquialgebra the norm is determined by the algebra, the involution and the datum,

$$
\lVert x\rVert = r(x \star x)^{1/2},
$$

the radius being the radius of the derived square, defined by invertibility alone.

*Proof.* The identity of the first section. $\square$

**Corollary (uniqueness and the contractive maps).** A $*$-algebra carries at most one $\mathrm{C}^{*}$-norm over the datum; every $*$-isomorphism of $\mathrm{C}^{*}$-sesquialgebras is isometric; and every unital $*$-homomorphism $\varphi : A \to B$ of $\mathrm{C}^{*}$-sesquialgebras is contractive, with

$$
\lVert\varphi(x)\rVert^{2} = r(\varphi(x) \star \varphi(x)) = r(\varphi(x \star x)) \leq r(x \star x) = \lVert x\rVert^{2} ;
$$

if $\varphi$ is injective the inequality is an equality and $\varphi$ is isometric.

*Proof.* Uniqueness: the formula writes the norm in the $*$-algebra, and the radius is defined by invertibility, an algebraic notion, so two $\mathrm{C}^{*}$-norms agree. A $*$-isomorphism preserves invertibility and hence the radius of the derived square, so it is isometric. Contractivity: for a unital homomorphism of complete normed algebras $\sigma(\varphi(y)) \subseteq \sigma(y)$ for the spectrum of the image, hence $r(\varphi(y)) \leq r(y)$; applied to $y = x \star x$ it gives the displayed chain, and for an injective map the spectral inclusion is an equality by the same argument applied to the inverse on the range. The statements and their proofs, in the complex case, are *The Involution and the Spectral Radius*, §*Rigidity*, and the layer adds to them the reading of $x \star x$ in place of $x^{*}x$. $\square$

### The Radius Is Not a Norm

**Remark (which axioms hold).** The spectral radius is homogeneous, $r(\lambda x) = \lvert\lambda\rvert r(x)$, it is bounded by the norm, $r(x) \leq \lVert x\rVert$, it is invariant on the spectral side of a product, $r(xy) = r(yx)$, and the derived square has $r(x \star x) = \lVert x\rVert^{2}$, the identity $r(x \star x) = r(x)^{2}$ holding exactly for the normal elements. It is nevertheless neither subadditive nor submultiplicative in the noncommutative case: for the two nilpotents

$$
N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad N^{\mathsf{T}} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
$$

one has $r(N) = r(N^{\mathsf{T}}) = 0$ while $r(N + N^{\mathsf{T}}) = r(NN^{\mathsf{T}}) = 1$, so neither $r(x+y) \leq r(x)+r(y)$ nor $r(xy) \leq r(x)r(y)$ survives the loss of commutativity; the witness is *The Involution and the Spectral Radius*, §*Rigidity*. Hence $r$ is a norm only on the commutative semisimple algebra, where Gelfand duality makes it the sup norm; in general it is not a norm but the constituent of the formula $\lVert x\rVert = r(x \star x)^{1/2}$, whose kernel is the set of quasi-nilpotent elements and which is a norm exactly because the derived square is taken before the radius.

## The Collapse at the Trivial Involution

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$, so that $R = k$ is an ordered field and the involution $*$ is $k$-linear. Then $\sigma(x^{*}) = \sigma(x)$, the elements with $x^{*} = x$ are the symmetric ones, $\lVert x\rVert^{2} = r(x^{*}x) = r(x \star x)$, the conclusions for the normal and the unitary elements are the statements of the bilinear layer, the contractivity of the unital $*$-homomorphisms is the statement for involutive Banach algebras, and the modulus is the absolute value of $k$.

*Proof.* Each statement is the corresponding one above read at $\varsigma = \mathrm{id}$: the twist of the spectrum is the identity map, the modulus is the absolute value, the derived operation is unchanged, and the objects are the complete normed involutive algebras of *Involutive Banach Algebras and the Gelfand–Naimark Theorem*. $\square$

**Remark (which statements are sesquilinear).** The identity, the formula for the norm, the rigidity and the contractivity hold in both kinds and are therefore not sesquilinear statements; the sesquilinear content of the article is the twist $\sigma(x^{*}) = \varsigma(\sigma(x))$, the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ in which the radius is measured, and the fact that a self-adjoint element of a complex base has real spectrum. The bilinear reading of the whole article is the theory of the involutive Banach algebra, and its completed form is *Involutive Banach Algebras and the Gelfand–Naimark Theorem*.

## Examples

### The Complex Matrices

**Example (the sesquilinear kind).** Let $R = \mathbb{C}$ with the conjugation, $A = M_{n}(\mathbb{C})$ with the conjugate transpose and the operator norm. The object is a $\mathrm{C}^{*}$-sesquialgebra, the involution is isometric, and the identities read $\lVert X\rVert^{2} = r(X^{*}X) = r(XX^{*}) = r(X \star X)$, with $\sigma(X^{*}) = \overline{\sigma(X)}$ the reflection of the spectrum. A Hermitian $X$ has real spectrum and $\lVert X\rVert = r(X) = \max\lvert\sigma(X)\rvert$; a normal $X$ the same; a unitary $X$ has spectrum on the unit circle and norm one. The nilpotents $N$, $N^{\mathsf{T}}$ of the preceding section show that the radius is not a norm: $\lVert N \star N\rVert = \lVert N^{\mathsf{T}} \star N^{\mathsf{T}}\rVert = 1$ by the identity, although $r(N) = r(N^{\mathsf{T}}) = 0$, the derived squares being the two complementary diagonal matrix units of the two-dimensional plane they span. The model is the one on which the layer's identities are read, and it is the finite-dimensional instance of *The Involution and the Spectral Radius*, §*Examples*.

### The Real Matrices

**Example (the bilinear kind).** Let $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $A = M_{n}(\mathbb{R})$ with the transpose and the operator norm. The involution is isometric and the object is a $\mathrm{C}^{*}$-sesquialgebra; the spectrum is fixed by the involution, $\sigma(X^{\mathsf{T}}) = \sigma(X)$, and a symmetric $X$ has real spectrum with $\lVert X\rVert = r(X)$, while a general normal real matrix need not have real spectrum: the rotation

$$
R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$

satisfies $R^{\mathsf{T}}R = RR^{\mathsf{T}} = 1$, so it is normal and unitary with $\lVert R\rVert = r(R) = 1$, and its spectrum is $\{\pm i\} \subseteq \mathbb{C} \setminus \mathbb{R}$; the spectrum of a self-adjoint element is real, and $R$ is not self-adjoint, $R^{\mathsf{T}} = -R$. The example separates the two clauses of the collapse: the twist of the spectrum is the identity map, and the radius is still the norm of a normal element, the spectrum being read in $\mathbb{C}$ although the scalars and the matrices are real.

### The Group Algebra

**Example (the isometric involution without the identity).** Let $G$ be a locally compact group and $A = L^{1}(G)$ with the convolution product, the involution $f^{*}(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the $L^{1}$-norm. The involution is isometric, hence continuous, so the object is a Banach sesquialgebra, and for $G = \mathbb{R}$ the $\mathrm{C}^{*}$-condition fails, the identity $\lVert f^{*}f\rVert_{1} = \lVert f\rVert_{1}^{2}$ being false for a general $f$; the radius computations of the example are *The Involution and the Spectral Radius*, §*Examples*, and the verdict is that the continuity of the involution and the $\mathrm{C}^{*}$-condition are independent hypotheses. The group algebra is *Group Algebras*, and its completion in the $\mathrm{C}^{*}$-norm, which exists and is unique by the corollary above, is the reduced group $\mathrm{C}^{*}$-algebra of the analysis layer.

### The Biquaternion Algebra

**Example (two norms on one $*$-algebra).** Let $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the Hermitian conjugation $* = {}^{\natural} \circ \bar{\cdot}$. The algebra is isomorphic, as a $*$-algebra, to $M_{2}(\mathbb{C})$ with the conjugate transpose through the isomorphism $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*, which carries $*$ to the dagger; transporting the operator norm along $\Phi$ makes $\mathbb{B}$ a $\mathrm{C}^{*}$-sesquialgebra, and then $\lVert\tilde{Q}\rVert^{2} = r(\tilde{Q} \star \tilde{Q})$ for every $\tilde{Q}$. The **Euclidean norm** of *The Norm Defined by a Form*, §*The Biquaternion Trace Form*, $\lVert\tilde{Q}\rVert_{E} = (\sum_\mu\lvert Q_\mu\rvert^{2})^{1/2}$, is a different complete norm on the underlying space, submultiplicative only up to the constant $\sqrt{2}$ of *The Euclidean Topology of the Biquaternion Algebra* and hence not an algebra norm, and it is **not** the $\mathrm{C}^{*}$-norm: at $\tilde{Q} = e_0 + ie_1$ one has $\lVert\tilde{Q}\rVert_{E}^{2} = 2$ while

$$
\tilde{Q} \star \tilde{Q} = (e_0 + ie_1)^{2} = 2e_0 + 2ie_1, \qquad \lVert\tilde{Q} \star \tilde{Q}\rVert_{E} = 2\sqrt{2},
$$

so the $\mathrm{C}^{*}$-condition fails for $\lVert\cdot\rVert_{E}$, and $\lVert\tilde{Q}\rVert_{E} = \sqrt{2}$ while the $\mathrm{C}^{*}$-norm of the same element is $2$. The example is the finite-dimensional companion of the group algebra above, the two witnessing together that the norms the layer attaches to a $*$-algebra need not be $\mathrm{C}^{*}$-norms, the group algebra as an isometric algebra norm and the Euclidean norm as the norm of the form; and it shows both halves of the rigidity: the $\mathrm{C}^{*}$-norm is unique once the condition holds, and the Euclidean norm of the form layer is not it.

## Summary

On a complete normed sesquialgebra over $(R,\varsigma)$ the involution and the norm are tied by the $\mathrm{C}^{*}$-condition $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$, and the tie is the formula $\lVert x\rVert = r(x \star x)^{1/2}$ in the derived square. The **spectrum is moved by the base involution**, $\sigma(x^{*}) = \varsigma(\sigma(x))$, so in the sesquilinear kind it is reflected, $\sigma(x^{*}) = \overline{\sigma(x)}$, and in the bilinear kind fixed, $\sigma(x^{*}) = \sigma(x)$; the radius is insensitive to the twist and the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ is the layer's absolute value. The radius of the **derived square** is the norm, $r(x \star x) = \lVert x \star x\rVert = \lVert x\rVert^{2}$, the element $x \star x$ being self-adjoint with nonnegative spectrum; the associative square has $r(x^{2}) = r(x)^{2} \leq \lVert x\rVert^{2}$, and the nilpotent witnesses $N$, $N^{\mathsf{T}}$ show that $r$ alone is neither subadditive nor submultiplicative, so the radius is the constituent of the formula and not the norm. For a normal element $\lVert x\rVert = r(x)$ and $r(x^{*}x) = r(x)^{2}$; a self-adjoint element has spectrum in the fixed field $k$ and norm equal to its radius; a unitary element has norm one and spectrum on the unit circle. The formula makes the norm an algebraic invariant, so a $*$-algebra carries at most one $\mathrm{C}^{*}$-norm, $*$-isomorphisms are isometric and unital $*$-homomorphisms are contractive, $\lVert\varphi(x)\rVert^{2} = r(\varphi(x \star x)) \leq r(x \star x) = \lVert x\rVert^{2}$, with equality for the injective ones. At $\varsigma = \mathrm{id}$ the twist is the identity map and the article collapses to the theory of involutive Banach algebras; the sesquilinear content is the twist of the spectrum and the reality of the spectrum of a self-adjoint element. The examples are the complex and the real matrices, the group algebra that is isometric without being a $\mathrm{C}^{*}$-algebra, and the biquaternion algebra, on which the Euclidean norm fails the $\mathrm{C}^{*}$-condition at $e_0 + ie_1$ and the operator norm is the unique $\mathrm{C}^{*}$-norm.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(R,\varsigma)$, $k = R^{\varsigma}$ | the base with $R = \mathbb{R}$, $\varsigma = \mathrm{id}$, or $R = \mathbb{C}$, $\varsigma$ the conjugation; the fixed field $k = \mathbb{R}$ |
| $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ | the modulus of the layer; the absolute value at $\varsigma = \mathrm{id}$ |
| $x \star y = xy^{*}$ | the derived operation, the product in which the identity is read |
| $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$ | the $\mathrm{C}^{*}$-condition, the axiom of the normed object |
| $\lVert x\rVert = r(x^{*}x)^{1/2} = r(x \star x)^{1/2}$ | the norm as the radius of the derived square |
| $x \star x = xx^{*}$, spectrum in $[0,\infty)$ | the derived square is self-adjoint and positive |
| $r(x \star x) = \lVert x\rVert^{2}$, $r(x^{2}) = r(x)^{2} \leq \lVert x\rVert^{2}$ | the derived square computes the norm, the associative square does not |
| $\sigma(x^{*}) = \varsigma(\sigma(x))$ | the spectrum under the involution; reflected at $\varsigma$ the conjugation |
| $\lvert\lambda\rvert \leq \lVert x\rVert$, $r(x) = \lim\lVert x^{n}\rVert^{1/n}$ | the elementary bound and the Gelfand–Beurling formula |
| normal $x$: $\lVert x\rVert = r(x)$, $r(x^{*}x) = r(x)^{2}$ | the normal case, containing the self-adjoint one |
| self-adjoint $x$: $\sigma(x) \subseteq k$, $\lVert x\rVert = r(x)$ | reality of the spectrum and the norm formula |
| unitary $x$: $\lVert x\rVert = 1$, $\sigma(x) \subseteq \{\lvert\lambda\rvert = 1\}$ | the unitary case |
| $\lVert\varphi(x)\rVert^{2} = r(\varphi(x \star x)) \leq r(x \star x) = \lVert x\rVert^{2}$ | contractivity, with equality for injective $*$-homomorphisms |
| $r(N + N^{\mathsf{T}}) = r(NN^{\mathsf{T}}) = 1$, $r(N) = r(N^{\mathsf{T}}) = 0$ | the radius is neither subadditive nor submultiplicative |
| $\varsigma = \mathrm{id}$ | the collapse: a linear involution, the spectrum fixed by it, the modulus the absolute value |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^{*}$-Algebras* (North-Holland, 1977), for the $\mathrm{C}^{*}$-identity, the uniqueness of the $\mathrm{C}^{*}$-norm and the isometric $*$-isomorphisms.
- Gérard J. Murphy, *$\mathrm{C}^{*}$-Algebras and Operator Theory* (Academic Press, 1990), for the spectral radius, the radius formula and the contractivity of the unital $*$-homomorphisms.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the spectrum of a self-adjoint element, its reality and the norm formula.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the spectral radius and the $\mathrm{C}^{*}$-norms of involutive Banach algebras, including the real case.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume II* (Cambridge University Press, 2001), for the comparison of the Banach $*$-norms and the uniqueness of the $\mathrm{C}^{*}$-norm.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the spectral radius of a bounded operator and the normal operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the algebras with involution over a field with involution.
