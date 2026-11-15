# __The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form at $n=4$__

## Introduction

**Every commutator map $\operatorname{ad}_A(X)=[A,X]$ is a derivation of $M_4(\mathbb{C})$, every derivation is of this form because the algebra is central simple, and the space of them is $\mathfrak{sl}_4$ of dimension $15$; the map is anti-self-adjoint for the trace form for every $A$ and anti-self-adjoint for the Hilbert–Schmidt form only when $A$ is anti-Hermitian, and the difference between the two statements is the involution, not the derivation.**

The article proves the Leibniz rule and the representation property, records the inner-derivation theorem with its dimension count, computes the two skewness conditions and their adjoints, determines the spectrum of $\operatorname{ad}_A$, and explains why the trace form cannot distinguish the symmetric from the antisymmetric directions while the Hilbert–Schmidt form can.

It assumes *The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$* and *The Derivations and the Automorphisms of $M_4(\mathbb{C})$*, where the inner-derivation theorem is proved in full. The case $n=2$ is *The Derivation Commutator and Its Skewness for the Trace Form*; the operator form is *The Adjoints and the Polar Decomposition of an Operator at $n=4$*.

## The Commutator Is a Derivation

**Proposition.** For every $A$, the map $\operatorname{ad}_A(X)=AX-XA$ satisfies the Leibniz rule $\operatorname{ad}_A(XY)=\operatorname{ad}_A(X)Y+X\operatorname{ad}_A(Y)$.

**Proof.** $A(XY)-(XY)A=(AX-XA)Y+X(AY-YA)$, by expanding both sides.

**Corollary.** $\operatorname{ad}_A$ is a derivation of $M_4$ for every $A$, and $\operatorname{ad}$ is linear in $A$.

**Proof.** The Leibniz rule is the definition of a derivation, and the map $A\mapsto\operatorname{ad}_A$ is linear by the bilinearity of the commutator.

**Proposition.** $\operatorname{ad}_{[A,B]}=[\operatorname{ad}_A,\operatorname{ad}_B]$, so $\operatorname{ad}$ is a homomorphism of Lie algebras from $\mathfrak{gl}_4$ into $\operatorname{Der}(M_4)$.

**Proof.** The Jacobi identity: $[[A,B],X]=[A,[B,X]]-[B,[A,X]]$, which is the commutator of the two maps applied to $X$.

**Corollary.** The image of $\operatorname{ad}$ is a Lie subalgebra of the derivations, isomorphic to $\mathfrak{gl}_4$ modulo its kernel.

**Proof.** The first isomorphism theorem for Lie algebras.

**The spectrum.** If $A$ is diagonalisable with eigenvalues $\lambda_1,\dots,\lambda_4$, the eigenvalues of $\operatorname{ad}_A$ on $M_4$ are the sixteen differences $\lambda_i-\lambda_j$.

**Proof.** In the eigenbasis of $A$, $\operatorname{ad}_A(E_{ij})=(\lambda_i-\lambda_j)E_{ij}$, and the sixteen units form a basis.

**Corollary.** $\operatorname{ad}_A$ is nilpotent exactly when $A$ has a single eigenvalue, and it is zero exactly when $A$ is a scalar.

**Proof.** All differences vanish exactly when all eigenvalues are equal, which over $\mathbb{C}$ means $A=\lambda\mathrm I+N$ with $N$ nilpotent; then $\operatorname{ad}_A=\operatorname{ad}_N$ is nilpotent.

## Every Derivation Is Inner

**Theorem.** Every derivation of $M_4(\mathbb{C})$ is inner: $\operatorname{Der}(M_4)=\operatorname{ad}(M_4)$, and the kernel of $\operatorname{ad}$ is the centre $\mathbb{C}\mathrm I_4$.

**Proof.** The kernel is the set of $A$ commuting with every matrix, which is the centre. Surjectivity is the theorem of the inner derivation, proved from the matrix units: a derivation is determined by its values on the sixteen units, and the element $a=\sum_{i,j}D(E_{ij})E_{ji}$ reproduces those values, the verification being the identity $D(E_{ij})=[a,E_{ij}]$ read off from $E_{ik}E_{kj}=E_{ij}$ summed over $k$.

**Corollary.** $\operatorname{Der}(M_4)\cong\mathfrak{gl}_4/\mathbb{C}\mathrm I_4\cong\mathfrak{sl}_4$, of dimension $15$.

**Proof.** The kernel has dimension $1$ and the source has dimension $16$.

**Corollary.** There are no outer derivations, and the Lie algebra of derivations is simple.

**Proof.** The quotient of $\mathfrak{gl}_4$ by the scalars is $\mathfrak{sl}_4$, which is simple.

**Why the theorem needs the algebra to be simple.** For a direct sum $A\oplus B$ the map sending a pair to the derivation $(a,b)\mapsto(0,\delta(b))$ with $\delta$ a derivation of $B$ is not inner in general; simplicity removes the summands, and centrality removes the scalar ambiguity.

**Proof.** A derivation of a direct sum acts on each summand and can be inner in one and outer in the other; the centre supplies the only ambiguity for a simple algebra.

## Skewness for the Trace Form

**Theorem.** For every $A$ and all $X,Y$,

$$
\beta(\operatorname{ad}_A X,Y)+\beta(X,\operatorname{ad}_A Y)=0,\qquad \beta(X,Y)=\operatorname{tr}(XY).
$$

**Proof.** Expand: $\operatorname{tr}((AX-XA)Y)+\operatorname{tr}(X(AY-YA))=\operatorname{tr}(AXY)-\operatorname{tr}(XAY)+\operatorname{tr}(XAY)-\operatorname{tr}(XYA)$, and the two middle terms cancel, leaving $\operatorname{tr}(AXY)-\operatorname{tr}(XYA)=0$ by the cyclic invariance of the trace.

**Corollary.** Every inner derivation lies in the orthogonal Lie algebra of $\beta$, which is $\mathfrak{so}(10,6)$ of dimension $120$; the fifteen inner derivations form a subalgebra of it.

**Proof.** Skewness for a bilinear form is the defining equation of its orthogonal Lie algebra, and $\mathfrak{so}(p,q)$ with $p+q=16$ has dimension $16\cdot15/2=120$.

**The trace form cannot detect the condition.** No hypothesis on $A$ is needed: the skewness is produced by the cyclic invariance of the trace alone, which holds for every triple of factors. The form is invariant under the whole of $\mathrm{GL}_4$, since $\operatorname{tr}(PXP^{-1}\cdot PYP^{-1})=\operatorname{tr}(XY)$, and the invariance is what produces the skewness.

**Proof.** Conjugation invariance of the trace, applied to the invariance identity $\beta(gXg^{-1},gYg^{-1})=\beta(X,Y)$ differentiated at the identity.

## Skewness for the Hilbert–Schmidt Form

**Definition.** $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$, positive definite.

**Proposition.** $\operatorname{ad}_A^{\ast}=\operatorname{ad}_{A^{\ast}}$ for the Hilbert–Schmidt form.

**Proof.** $\langle\operatorname{ad}_A X,Y\rangle=\operatorname{tr}((AX-XA)^{\ast}Y)=\operatorname{tr}(X^{\ast}A^{\ast}Y)-\operatorname{tr}(A^{\ast}X^{\ast}Y)=\langle X,A^{\ast}Y\rangle-\langle X,YA^{\ast}\rangle=\langle X,\operatorname{ad}_{A^{\ast}}Y\rangle$ after moving $A^{\ast}$ to the right by cyclicity.

**Corollary.** $\operatorname{ad}_A$ is anti-self-adjoint for the Hilbert–Schmidt form exactly when $A$ differs from an anti-Hermitian matrix by a real scalar.

**Proof.** Skewness is $\operatorname{ad}_{A^{\ast}}=-\operatorname{ad}_A$, that is $A^{\ast}+A\in\mathbb{C}\mathrm I_4$; writing $A^{\ast}+A=\mu\mathrm I$ and taking adjoints gives $\bar\mu=\mu$, so $\mu$ is real and $A-\tfrac{\mu}{2}\mathrm I_4$ is anti-Hermitian, with the same adjoint map since the scalar part is central.

**Corollary.** The derivations that are anti-self-adjoint for the Hilbert–Schmidt form are exactly those of $\operatorname{ad}\mathfrak{u}(4)$, of dimension $15$.

**Proof.** The anti-Hermitian matrices form $\mathfrak{u}(4)$ of real dimension $16$, and the scalars in it are the single imaginary line, so the image has dimension $15$.

**The adjoint is a different operator.** For the trace form the adjoint of $\operatorname{ad}_A$ is $-\operatorname{ad}_A$; for the Hilbert–Schmidt form it is $\operatorname{ad}_{A^{\ast}}$, which is a different derivation unless $A$ is anti-Hermitian.

**Proof.** Compare the two displayed formulas.

## The Difference Is the Involution

**Proposition.** The condition for skewness for $\beta$ involves no involution; the condition for skewness for $\langle\cdot,\cdot\rangle$ involves the adjoint ${}^{\ast}$.

**Proof.** The first condition is an identity in $A$, the second is the equation $A^{\ast}+A\in\mathbb{C}\mathrm I$.

**Corollary.** The trace form sees the whole of $\mathfrak{gl}_4$ inside $\mathfrak{so}(10,6)$, while the Hilbert–Schmidt form sees only $\mathfrak{u}(4)$ inside $\mathfrak{so}(16)$.

**Proof.** The two invariance groups are $\mathrm{GL}_4$ and $U(4)$, and the Lie algebras of anti-self-adjoint endomorphisms contain the respective images of $\operatorname{ad}$.

**The moral.** Every derivation is anti-self-adjoint for the trace form because that form is invariant under the largest possible group; a derivation is anti-self-adjoint for the Hilbert–Schmidt form only when its generator lies in the Lie algebra of the smaller group. The involution ${}^{\ast}$ chooses the smaller group, and the derivation is the same object in both statements.

**The two halves of the statement.** For $A$ symmetric, $\operatorname{ad}_A$ is anti-self-adjoint for $\beta$ and self-adjoint for $\langle\cdot,\cdot\rangle$; for $A$ antisymmetric, it is anti-self-adjoint for both.

**Proof.** For symmetric $A$, $A^{\ast}=A$, so $\operatorname{ad}_A^{\ast}=\operatorname{ad}_A$; for antisymmetric $A$, $A^{\ast}=-A$, so the adjoint is $-\operatorname{ad}_A$.

**Corollary.** The space of inner derivations has dimension $15$, the dimension of $\mathfrak{sl}_4$, since the scalars act by zero and every traceless matrix gives a nonzero derivation.

**Proof.** The kernel of $A\mapsto\operatorname{ad}_A$ is the centre, which is the scalars.

## Summary

The commutator map is a derivation for every element, the representation property holds by the Jacobi identity, and every derivation of the algebra is inner, so the derivations form $\mathfrak{sl}_4$ of dimension $15$.

The map is anti-self-adjoint for the trace pairing for every $A$, with no condition, because the trace is cyclically invariant; it is anti-self-adjoint for the Hilbert–Schmidt form exactly when $A$ is anti-Hermitian up to a real scalar, that is when the derivation lies in $\operatorname{ad}\mathfrak{u}(4)$.

The difference between the two statements is the involution and not the derivation: the trace form is invariant under all of $\mathrm{GL}_4$, the Hilbert–Schmidt form only under $U(4)$, and the adjoint needed for the second statement is built from the conjugate transpose. The spectrum of $\operatorname{ad}_A$ is the sixteen differences of eigenvalues, and the kernel is the centraliser, of dimension at least four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_A(X)=[A,X]$ | the inner derivation |
| $\operatorname{Der}(M_4)$ | the derivations, isomorphic to $\mathfrak{sl}_4$ |
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the trace pairing |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$ | the Hilbert–Schmidt form |
| $\mathfrak{so}(10,6)$ | the orthogonal Lie algebra of $\beta$ |
| $\operatorname{ad}\mathfrak{u}(4)$ | the derivations anti-self-adjoint for the Hilbert–Schmidt form |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the theorem that every derivation of a central simple algebra is inner.
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for the full proof of the inner-derivation theorem.
- [The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-signature-on-the-two-halves-of-m4c.html), for the form whose invariance produces the skewness.
- [The Hilbert–Schmidt Form at $n=4$](the-hilbert-schmidt-form-at-n-4.html), for the positive definite form of the second statement.
- [The Derivation Commutator and Its Skewness for the Trace Form](the-derivation-commutator-and-its-skewness-for-the-trace-form.html), for the same two statements at order two.
