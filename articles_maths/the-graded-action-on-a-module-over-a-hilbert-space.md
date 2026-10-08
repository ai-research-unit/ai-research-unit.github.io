# __The Graded Action on a Module over a Hilbert Space__

## Introduction

A module over a Hilbert space is a module over the graded algebra $B(H)$ of the bounded operators of that Hilbert space, and a **graded action** is an action that respects the grading: a homogeneous operator of degree $i$ sends the degree-$j$ part of the module to the degree-$(i+j)$ part. The graded action is therefore a representation of a graded algebra in which the degree is additive rather than merely preserved, and the sign that appears in the graded commutator is exactly the sign that makes the representation a homomorphism of graded algebras. The analytic content of the Hilbert-space case is that the module is a graded Hilbert space, the action is by bounded operators, and a graded action of a $C^*$-algebra is automatically contractive and intertwines the two parity operators.

This article fixes the graded module over the graded algebra $B(H)$, the graded action and its sign rule, the parity operator of the module and its intertwining with the action, the boundedness and the block form of the action, and the relation to the graded actions of the abstract theory. The graded algebra $B(H)$ and the grade involution are *The Signed Sandwich on a Hilbert Space* and *Reflections as Signed Two-Sided Operators on a Hilbert Space*; the abstract graded module and its sign rule are *The Graded Action on a Module over a Graded Algebra* (Part II), of which the present article is the Hilbert-space reading; the module theory over a ring is *Modules over a Ring* (Part I), and the adjoint of the graded action is *The Graded Adjoint Action on a Module over a Hilbert Space* below.

Throughout, $H=H^0\oplus H^1$ is a graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with parity operator $\Gamma$, and $B(H)=B(H)^0\oplus B(H)^1$ is the graded algebra of bounded operators, where $B(H)^i=\{T:\alpha(T)=(-1)^iT\}$. A **graded module** is a graded Hilbert space $M=M^0\oplus M^1$ with parity operator $\Gamma_M$ together with a bounded action $\rho:B(H)\to B(M)$. Degrees are read in $\mathbb{Z}/2$.

## Graded Modules over the Graded Algebra

**Definition.** A **graded module over a Hilbert space** is a graded Hilbert space $M=M^0\oplus M^1$ with a bounded linear map $\rho:B(H)\to B(M)$ such that

$$
\rho\bigl(B(H)^i\bigr)M^j\subseteq M^{i+j}
$$

for $i,j\in\mathbb{Z}/2$; the action is written $T\cdot m=\rho(T)m$.

**Proposition (the module axioms).** A graded action is a module action, $\rho(ST)=\rho(S)\rho(T)$ and $\rho(I)=\mathrm{id}_M$, and the grading is compatible with the action in the strong sense that the even operators of $B(H)$ act as even operators of $M$ and the odd operators act as odd operators:

$$
\rho(T)M^j\subseteq M^j\ (T\ \text{even}),\qquad \rho(T)M^j\subseteq M^{1+j}\ (T\ \text{odd}).
$$

The module is a module in the ordinary sense when the grading is forgotten.

*Proof.* The action is a homomorphism by definition, and the grading condition is the additivity of the degree; the last statement is the definition read without the grading.

**Proposition (intertwining of the parity operators).** A bounded action $\rho$ is graded if and only if it intertwines the two parity operators,

$$
\rho(T)\,\Gamma_M=(-1)^{|T|}\,\Gamma_M\,\rho(T)\quad\text{on homogeneous }T,
$$

equivalently $\rho(\Gamma_H)=\Gamma_M$ when $\rho$ is a $*$-homomorphism, and the even part of the action is the subalgebra $\rho(B(H)^0)$, which preserves each graded piece.

*Proof.* A homogeneous $T$ of degree $i$ has $\Gamma_H T\Gamma_H=(-1)^iT$; applying $\rho$ gives $\rho(\Gamma_H)\rho(T)\rho(\Gamma_H)=(-1)^i\rho(T)$ and, if the action is a $*$-homomorphism, $\rho(\Gamma_H)=\Gamma_M$ by the intertwining; the grading condition and the intertwining are then the same statement.

**Proposition (the graded dual and the degree).** The **graded dual** $M^\vee$ is the graded Hilbert space with $(M^\vee)^i=(M^i)^*$, its elements are the bounded functionals, and the evaluation pairing $\langle f,m\rangle=f(m)$ has degree zero, vanishing unless $|f|=|m|$; the shift $M[1]$ has $(M[1])^i=M^{i+1}$ and satisfies $(M[1])^\vee=M^\vee[1]$.

*Proof.* A bounded functional on $M$ restricts to each graded piece, and the dual of a direct sum is the direct sum of the duals; the pairing of $(M^i)^*$ with $M^j$ vanishes for $i\neq j$ and has degree zero as an element of $\mathbb{Z}/2$; the shift statement is the reindexing of the summands.

## The Graded Action and the Sign Rule

**Definition.** For homogeneous elements $S,T$ of $B(H)$ the **graded commutator** is

$$
[S,T]_{\mathrm{gr}}=ST-(-1)^{|S||T|}TS,
$$

and the action is a **graded action** when the module carries the grading and the representation respects it, $\rho(B(H)^i)M^j\subseteq M^{i+j}$.

**Theorem (the sign rule is forced by multiplicativity).** Let $\rho$ be a graded action of $B(H)$ on $M$. Then for homogeneous $S,T$ the graded commutator is preserved:

$$
\rho\bigl([S,T]_{\mathrm{gr}}\bigr)=[\rho(S),\rho(T)]_{\mathrm{gr}} .
$$

The sign $(-1)^{|S||T|}$ is the unique sign for which multiplicativity and the grading are compatible; with the ordinary commutator $ST-TS$ in its place the identity fails for two odd elements.

*Proof.* Expanding $\rho(ST)$ and $\rho(TS)$ by multiplicativity and applying the graded sign gives the identity. Two odd elements have $(-1)^{|S||T|}=-1$, so the graded commutator of the images is $\rho(S)\rho(T)+\rho(T)\rho(S)$ while the ordinary commutator is $\rho(S)\rho(T)-\rho(T)\rho(S)$, and the two differ by the anticommutator, which need not vanish.

**Proposition (the sign rule on homogeneous vectors).** For homogeneous $T,S\in B(H)$ and $m\in M$,

$$
T\cdot m\in M^{|T|+|m|},\qquad S\cdot(T\cdot m)=(-1)^{|S||T|}\,T\cdot(S\cdot m)+[S,T]_{\mathrm{gr}}\cdot m ,
$$

so the action of an odd operator changes the degree of the vector, and the two orders of two homogeneous actions differ by the Koszul sign and the graded commutator.

*Proof.* The additivity of the degree is the defining condition; the identity is the graded commutator $ST=(-1)^{|S||T|}TS+[S,T]_{\mathrm{gr}}$ acting on $m$ and read through multiplicativity of $\rho$.

**Remark.** The sign rule is the difference between a graded action and a representation that merely preserves degrees: an action that is only degree-preserving need not be a homomorphism, and its failure is precisely a discrepancy in the graded commutator. The Hilbert-space theory keeps the sign because the grading is given by conjugation by $\Gamma$, and multiplicativity of $\rho$ on the two homogeneous parts is multiplicativity of the representation.

## Boundedness and the Parity Operator

**Theorem (a graded action of a $C^*$-algebra is contractive).** Every action $\rho$ of $B(H)$ by bounded operators on the Hilbert space $M$ satisfies

$$
\|\rho(T)\|\le\|T\| ,
$$

with equality exactly when $\rho$ is injective; in particular a graded action of $B(H)$ is a contraction, and it is an isometry exactly when it is faithful.

*Proof.* The action is a $*$-homomorphism of a $C^*$-algebra into $B(M)$, and a $*$-homomorphism of $C^*$-algebras is contractive; injectivity makes it isometric by the $C^*$-identity. The graded case is a special case, the grading being given by the conjugation by $\Gamma_H$ and transported to $M$.

**Proposition (the even part and the commutant).** The even part $\rho(B(H)^0)$ preserves each graded piece, and its restriction to $M^j$ is a representation of the even subalgebra; the parity operator $\Gamma_M$ commutes with the even part and anticommutes with the odd part, so the commutant of $\rho(B(H))$ is the set of operators commuting with both $\rho(B(H)^0)$ and $\rho(\Gamma_H)$.

*Proof.* The preservation of the pieces is the grading condition with $i=0$; the commutation relations are the intertwining of the previous section, and the statement about the commutant is the definition of the commutant read on the two pieces.

**Remark (the $*$-structure).** When the module is a **Hilbert module**, meaning that $M$ carries an inner product for which each $\rho(T)$ has an adjoint and $\rho(T^*)=\rho(T)^*$, the graded action is a graded $*$-representation, the odd operators are skew-adjoint with respect to the grading, and the sign rule is compatible with the involution, $\rho((ST)^*)=\rho(T^*)\rho(S^*)$. The general theory of Hilbert modules is *Hilbert Algebras* and *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* (Part II).

## The Block Form and the Even Part

**Definition.** In the decomposition $M=M^0\oplus M^1$ a bounded operator is written in block form $T=\begin{pmatrix}P&Q\\R&S\end{pmatrix}$ with $P:M^0\to M^0$, $Q:M^1\to M^0$, $R:M^0\to M^1$, $S:M^1\to M^1$; the operator is even exactly when $Q=R=0$ and odd exactly when $P=S=0$.

**Proposition (the graded action in blocks).** For a graded action $\rho$ and homogeneous $T\in B(H)$ of degree $i$, the block form of $\rho(T)$ has nonzero blocks only between pieces whose degrees differ by $i$:

$$
\rho(T)=\begin{pmatrix}P&0\\0&S\end{pmatrix}\ (i=0),\qquad
\rho(T)=\begin{pmatrix}0&Q\\R&0\end{pmatrix}\ (i=1),
$$

and the parity operator of the module is $\Gamma_M=\operatorname{diag}(P^0,-P^1)$ with $P^j$ the projection onto $M^j$.

*Proof.* The grading condition $\rho(B(H)^i)M^j\subseteq M^{i+j}$ says that the component of $\rho(T)$ sending $M^j$ to $M^{j+i}$ is the only one that can be nonzero; for $i=0$ this permits the diagonal blocks, and for $i=1$ only the off-diagonal blocks, which is the block form displayed.

**Example (the regular module).** The algebra $B(H)$ is a graded module over itself with $\rho(T)=L_T$ the left multiplication; the graded pieces are the even and odd operators, the action of an odd element sends the even part to the odd part, and the parity operator is the grade involution $\alpha$, which commutes with the even left multiplications and anticommutes with the odd ones.

**Example (a module of finite rank over the matrix algebra).** For $H=\mathbb{K}^{p+q}$ and $M=\mathbb{K}^{r+s}$, a graded action of $M_{p+q}(\mathbb{K})$ on $M$ is given by a block matrix representation in which the even generators act diagonally and the odd generators act off-diagonally; the commutant is the algebra of operators commuting with the parity and with the even part, realising the double commutant statement of the graded theory in finite dimension.

## Summary

A graded module over a Hilbert space is a graded Hilbert space $M=M^0\oplus M^1$ carrying a bounded action of the graded algebra $B(H)$ such that $\rho(B(H)^i)M^j\subseteq M^{i+j}$; the action is an ordinary module action together with the additivity of the degree, equivalently the intertwining $\rho(\Gamma_H)=\Gamma_M$ of the two parity operators, and in block form the even operators act diagonally and the odd operators off-diagonally. The graded commutator $[S,T]_{\mathrm{gr}}=ST-(-1)^{|S||T|}TS$ carries the Koszul sign, and that sign is the unique one making the action a representation of the graded algebra; without it the action is only degree-preserving and need not be multiplicative. A graded action of the $C^*$-algebra $B(H)$ is automatically contractive, $\|\rho(T)\|\le\|T\|$, and isometric exactly when faithful; with an inner product for which each action is a $*$-homomorphism the module is a Hilbert module and the action is a graded $*$-representation. The regular module with $\rho=L$ and the finite-rank matrix modules are the standard examples, and the adjoint version of the action, in which the sign appears in the transpose, is *The Graded Adjoint Action on a Module over a Hilbert Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(H)=B(H)^0\oplus B(H)^1$ | the graded algebra of bounded operators |
| $\alpha(T)=\Gamma T\Gamma$ | the grade involution, $\alpha(T)=(-1)^iT$ on $B(H)^i$ |
| $M=M^0\oplus M^1$ | the graded Hilbert module |
| $\rho(B(H)^i)M^j\subseteq M^{i+j}$ | the graded action condition |
| $\rho(\Gamma_H)=\Gamma_M$ | intertwining of the parity operators |
| $[S,T]_{\mathrm{gr}}=ST-(-1)^{|S||T|}TS$ | the graded commutator |
| $\|\rho(T)\|\le\|T\|$ | contractivity of the $C^*$-action |
| $\rho(T)=\begin{pmatrix}P&0\\0&S\end{pmatrix}$ or $\begin{pmatrix}0&Q\\R&0\end{pmatrix}$ | block form of even and odd actions |
| $M^\vee$, $M[1]$ | graded dual and shift |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for representations of $B(H)$ and the contractivity of $C^*$-homomorphisms.
- Marc A. Rieffel, "Induced Representations of $C^*$-algebras", *Advances in Mathematics* **13** (1974), 176–257, for the module-theoretic reading of representations of operator algebras.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry", in *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the Koszul sign rule and graded modules.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the graded module theory and the sign rule in the graded category.
- E. Christopher Lance, *Hilbert $C^*$-Modules* (Cambridge University Press, 1995), for Hilbert modules over operator algebras and their graded actions.
