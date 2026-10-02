
# __The Graded Action on a Module over a Clifford Algebra__

## Introduction

A Clifford algebra is a $\mathbb{Z}/2$-graded algebra, with the even elements $\mathrm{Cl}^0$ and the odd elements $\mathrm{Cl}^1$, and its modules carry the same grading when the action respects it: a **graded module** is a vector space $S=S^0\oplus S^1$ with a module structure such that $\mathrm{Cl}^i\cdot S^j\subseteq S^{i+j}$. The action is then represented by a map that is **parity-preserving**, $c(\mathrm{Cl}^i)\subseteq\mathrm{End}^i(S)$, so that even elements act by even operators and odd elements by odd ones. This is the sign rule of the category: the same algebra element acts by an operator of a definite parity, the graded commutator replaces the commutator in the relations, and the maps between graded modules must carry the parity factor in the intertwining relation. The article sets out the graded module structure, the compatibility of the action with the grading, and the sign rule that this compatibility imposes.

The geometric reading is the chirality grading. The module grading of a Clifford module is the decomposition of a spinor bundle into its two chiral halves, the parity of the operator $c(v)$ for a vector is the statement that the Clifford multiplication exchanges the halves, and the parity of the Cauchy–Riemann operator is the analytic consequence: $D$ is an odd operator and therefore exchanges the chiral summands. The sign rule is what makes the parity a rule and not a convention, and the two examples that keep the account concrete are the exterior algebra $\Lambda^\bullet V$ with $c(v)=v\wedge-\iota_v$ and the spinor module with the chirality operator.

**The boundaries.** The parity of the one-sided and two-sided multiplication operators is *One-Sided Operators on a Clifford Algebra* and *The Two-Sided Multiplication Operators*; the twisting of those operators by the grading is *The Graded Multiplication Operators*; the module theory of the regular module is *Left Multiplication and the Clifford Module Structure*; the abstract algebra of the grading is *Clifford Algebras* and its companions in Part II. The chirality operator of the spinor bundle and the parity of the Cauchy–Riemann operator are *Spin Geometry* and *The Spinor Operator*. The base is a field $F$ of characteristic not $2$, $q$ a quadratic form with $q(u)=B(u,u)$ and $uv+vu=2B(u,v)$, and a $\mathbb{Z}/2$-graded module (a supermodule) over $\mathrm{Cl}(V,q)$.

## The Graded Module Structure

### Definition and Parity

**Definition.** A **graded module** over $\mathrm{Cl}(V,q)$ is a $\mathbb{Z}/2$-graded vector space $S=S^0\oplus S^1$ with a bilinear multiplication $\mathrm{Cl}(V,q)\times S\to S$ that is a module action and satisfies $\mathrm{Cl}^i\cdot S^j\subseteq S^{i+j}$. A **graded endomorphism** of $S$ is a linear map preserving the grading, an **odd** endomorphism one exchanging the two summands, and $\mathrm{End}(S)$ is the graded algebra of all endomorphisms with the parity so defined.

**Proposition.** The action of a homogeneous element $a\in\mathrm{Cl}^i$ on $S$ is an operator of parity $i$, and the assignment $c(a)\in\mathrm{End}^i(S)$ is an algebra homomorphism that preserves the parity and the relations: for vectors $u,v$,

$$
c(u)c(v)+c(v)c(u) = 2B(u,v)\operatorname{id}_S ,
$$

and every relation of $\mathrm{Cl}(V,q)$ holds in $\mathrm{End}(S)$ with the same signs.

**Proof.** The inclusion $\mathrm{Cl}^iS^j\subseteq S^{i+j}$ says exactly that the operator of $a\in\mathrm{Cl}^i$ maps $S^j$ into $S^{i+j}$, which is parity $i$. The action being a module action means $c(a)c(b)=c(ab)$, a homomorphism; the Clifford relations are their images in the endomorphism algebra. The parity preservation of the homomorphism is read off the grading inclusions.

**Remark (the parity is not a choice).** The exponent in the grading is the same $\mathbb{Z}/2$ that grades the algebra, and the relations of the module use the same parity: the sign of $c(a)c(b)$ relative to $c(b)c(a)$ is fixed by the degrees of $a$ and $b$, not chosen. This is why the parity enters every formula of the graded category and only as the Koszul sign below.

### The Graded Commutator

**Definition.** The **graded commutator** of homogeneous operators $A,B\in\operatorname{End}(S)$ is

$$
[A,B\} = AB - (-1)^{|A||B|}BA .
$$

For odd $A,B$ it is the anticommutator $AB+BA$, and for even $A$ or $B$ it is the ordinary commutator.

**Proposition.** The Clifford relations are the statement that the Clifford multiplication is a **graded representation**: for homogeneous $a,b\in\mathrm{Cl}(V,q)$,

$$
[c(a),c(b)\} = c([a,b\}) ,
$$

where the bracket on the right is the graded commutator in the Clifford algebra; for vectors $u,v$ this is $c(u)c(v)+c(v)c(u)=2B(u,v)\operatorname{id}$, and for an even element with any element it is the ordinary commutator.

**Proof.** The graded commutator is bilinear and respects the parity; the homomorphism $c$ carries the graded commutator of the algebra to the graded commutator of the operators, which is the defining compatibility of a homomorphism of graded algebras. For two odd vectors the graded bracket is the anticommutator, giving the Clifford relation.

**Remark.** The graded commutator is the reason the Clifford algebra is the quantisation of the graded Poisson bracket of the exterior algebra: the exterior algebra with $c(v)=v\wedge-\iota_v$ is a module over the Clifford algebra, and the parity of $c(v)$ is odd, so the anticommutator is the relation and the $\mathbb{Z}/2$-grading of $\Lambda^\bullet V$ is the module grading.

## The Sign Rule for Maps

### Intertwiners

**Definition.** A linear map $f : S\to S'$ of graded Clifford modules is **even** if $f(S^j)\subseteq (S')^j$ and **odd** if $f(S^j)\subseteq (S')^{j+1}$. An intertwiner of a definite parity is one satisfying

$$
f(c(a)s) = (-1)^{|f|\,|a|}\,c(a)f(s)
$$

for homogeneous $a$.

**Theorem.** Let $f$ be a homogeneous linear map of graded Clifford modules. Then $f$ is a module map if and only if it satisfies the displayed sign rule; for an even intertwiner the sign disappears and the relation is the ordinary one, and for an odd intertwiner the parity factor $(-1)^{|a|}$ is present.

**Proof.** A module map is a map with $f(ax)=af(x)$ for all $a,x$; if the map is even, this is the stated relation with sign $+1$. If the map is odd, the two sides of the naive relation lie in opposite components, and the correct relation is obtained by composing with the parity operator; the factor $(-1)^{|a|}$ is exactly the comparison of the two sides for a homogeneous $a$. The rule is the Koszul sign in the supercategory, stated for linear maps rather than for the tensor product.

**Remark (why the sign is forced).** The sign $(-1)^{|f||a|}$ is not a convention: an odd map sends the even part of the source to the odd part of the target, and the module action on a homogeneous element moves the component by $|a|$; the composition of the two parity shifts must be matched, which fixes the sign. The same rule governs the graded tensor product $S\hat\otimes T$ of two graded modules, where $(x\hat\otimes y)(a\hat\otimes b) = (-1)^{|y||a|}(xa)\hat\otimes(yb)$; this is *The Graded Multiplication Operators*.

### Odd Operators and the Chirality

**Proposition.** Let $S=S^0\oplus S^1$ be a graded Clifford module and $D$ an odd operator acting on the sections of $S$ that commutes with the module action; then $D$ maps the sections of $S^0$ to those of $S^1$ and vice versa, and its square is an even operator preserving each summand. For the Cauchy–Riemann operator on a spinor bundle with the chirality grading, $D$ is odd and the chirality decomposition is $D=D^+\oplus D^-$ with $D^\pm:\Gamma(\mathcal{S}^\pm)\to\Gamma(\mathcal{S}^\mp)$.

**Proof.** An odd operator exchanges the two summands by definition; the square of an odd operator is even and preserves each summand; the identification of the parity of the Cauchy–Riemann operator with the chirality is *The Spinor Operator*, where $D$ anticommutes with the chirality operator.

**Remark (the parity of the curvature).** The square $D^2$ is even, and its two summands $D^-D^+$ and $D^+D^-$ are the Laplacians of the two chiral halves; the index of the pair is the Fredholm index of $D^+$. This is the analytic form of the chirality grading, and it is the reason the index theorem of *Spin Geometry* is a statement about the odd part of an odd operator.

## Worked Cases

### The Exterior Algebra

On $\Lambda^\bullet V=\bigoplus_j\Lambda^jV$ the grading is the form degree reduced modulo two, and the multiplication $c(v)=v\wedge-\iota_v$ is an odd operator: the exterior multiplication raises the degree by one and the interior multiplication lowers it by one, so the parity is odd. The relations $c(v)c(w)+c(w)c(v)=2B(v,w)\operatorname{id}$ hold as the graded commutator relation of the proposition, and the module is the canonical graded Clifford module of the algebra.

### The Spinor Module

For $\dim V$ even and $q$ definite, the spinor module $S$ splits into the two half-spin modules $S^0\oplus S^1$ under the volume element, the multiplication by a vector is odd and exchanges them, and the module of endomorphisms of $S$ splits into the even and odd intertwiners. The sign rule governs every equivariant map between spinor modules, and the two irreducible half-spin modules are the two simple summands of the grading.

### A One-Dimensional Module

For $\dim V=1$ with $q(u)\ne0$, the module $S=F\oplus F$ with $c(u)$ swapping the two summands is a graded module, the operator $c(u)$ is odd with square $q(u)$, and the even intertwiners are the diagonal scalars and the odd intertwiners the off-diagonal ones. The sign rule is visible in the single nontrivial relation $f(c(u)s)=(-1)^{|f|}c(u)f(s)$.

## Summary

A **graded module** $S=S^0\oplus S^1$ over a Clifford algebra is a module whose multiplication respects the parity, $\mathrm{Cl}^iS^j\subseteq S^{i+j}$; the action is then a parity-preserving algebra homomorphism $c$ with $c(\mathrm{Cl}^i)\subseteq\mathrm{End}^i(S)$, and the Clifford relations hold in the graded form $[c(a),c(b)\}=c([a,b\})$, which for vectors is the anticommutator $c(u)c(v)+c(v)c(u)=2B(u,v)\operatorname{id}$. The **sign rule** is the compatibility of the grading with the maps: a homogeneous module map of parity $|f|$ satisfies $f(c(a)s)=(-1)^{|f||a|}c(a)f(s)$, the even intertwiners have the ordinary relation and the odd ones carry the Koszul sign; the same sign governs the graded tensor product. The geometric reading is the chirality grading of a spinor bundle: the multiplication by a vector is odd and exchanges the chiral halves, the Cauchy–Riemann operator is odd with $D=D^+\oplus D^-$, and its square is even with the two chiral Laplacians as summands. The twisting of the one-sided operators is *The Graded Multiplication Operators*; the module theory is *Left Multiplication and the Clifford Module Structure*; the chirality in geometry is *Spin Geometry* and *The Spinor Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=S^0\oplus S^1$ | Graded (super) Clifford module |
| $\mathrm{Cl}^iS^j\subseteq S^{i+j}$ | Compatibility of the action with the grading |
| $c(\mathrm{Cl}^i)\subseteq\mathrm{End}^i(S)$ | Parity of the action |
| $[A,B\}=AB-(-1)^{\lvert A\rvert\lvert B\rvert}BA$ | Graded commutator |
| $[c(a),c(b)\}=c([a,b\})$ | Graded representation property |
| $f(c(a)s)=(-1)^{\lvert f\rvert\lvert a\rvert}c(a)f(s)$ | Sign rule for a homogeneous module map |
| $(x\hat\otimes y)(a\hat\otimes b)=(-1)^{\lvert y\rvert\lvert a\rvert}(xa)\hat\otimes(yb)$ | Koszul sign in the graded tensor product |
| $c(v)=v^\flat\wedge-\iota_v$ on $\Lambda^\bullet V$ | Canonical odd example |
| $D=D^+\oplus D^-$ | Odd Cauchy–Riemann operator and the chirality split |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality grading, the parity of the Clifford multiplication and the oddness of the Dirac-type operators.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry", in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the sign rule and the supercategory.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for graded modules, the Koszul sign and the graded tensor product.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the supermodule structure of the Clifford bundle and the chirality decomposition.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grading and the parity of the operators it produces.
